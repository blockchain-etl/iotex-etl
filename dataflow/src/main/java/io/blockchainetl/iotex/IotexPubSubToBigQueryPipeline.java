package io.blockchainetl.iotex;

import com.google.common.collect.Lists;
import io.blockchainetl.iotex.fns.EntityJsonToTableRow;
import io.blockchainetl.iotex.utils.FileUtils;
import org.apache.beam.sdk.Pipeline;
import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO;
import org.apache.beam.sdk.io.gcp.bigquery.InsertRetryPolicy;
import org.apache.beam.sdk.io.gcp.bigquery.WriteResult;
import org.apache.beam.sdk.io.gcp.pubsub.PubsubIO;
import org.apache.beam.sdk.options.PipelineOptionsFactory;
import org.apache.beam.sdk.options.ValueProvider;

import java.util.List;


public class IotexPubSubToBigQueryPipeline {

    private static final String PUBSUB_ID_ATTRIBUTE = "item_id";

    public static void main(String[] args) {
        PubSubToBigQueryPipelineOptions options =
            PipelineOptionsFactory.fromArgs(args).withValidation().as(PubSubToBigQueryPipelineOptions.class);

        Pipeline pipeline = Pipeline.create(options);

        List<String> entityNames = Lists.newArrayList("blocks", "actions", "logs", "transaction_logs");

        for (String entityName : entityNames) {
            buildPipelineForEntity(pipeline, options, entityName);
        }

        pipeline.run();
    }

    private static void buildPipelineForEntity(
        Pipeline pipeline, PubSubToBigQueryPipelineOptions options, String entityName) {
        String transformNamePrefix = options.getTransformNamePrefix();

        WriteResult writeResult = pipeline
            .apply(transformNamePrefix + "PubSubListener", PubsubIO.readStrings()
                .fromSubscription(ValueProvider.NestedValueProvider.of(options.getPubSubSubscriptionPrefix(), input -> input + "." + entityName))
                .withIdAttribute(PUBSUB_ID_ATTRIBUTE))
            .apply(transformNamePrefix + "WriteToBigQuery", BigQueryIO.<String>write()
                .to(ValueProvider.NestedValueProvider.of(options.getBigQueryDataset(), input -> input + "." + entityName))
                .withFormatFunction(new EntityJsonToTableRow())
                .ignoreUnknownValues()
                .withCreateDisposition(BigQueryIO.Write.CreateDisposition.CREATE_NEVER)
                .withWriteDisposition(BigQueryIO.Write.WriteDisposition.WRITE_APPEND)
                .withoutValidation()
                .withExtendedErrorInfo()
                .withMethod(BigQueryIO.Write.Method.STREAMING_INSERTS)
                .withFailedInsertRetryPolicy(InsertRetryPolicy.retryTransientErrors()));

        writeResult.getFailedInsertsWithErr()
            .apply(transformNamePrefix + "BigQueryErrorsSink", new BigQueryErrorsSink(
                options.getOutputErrorsTable(), FileUtils.readFileFromClasspath("errors-schema.json")));
    }
}
