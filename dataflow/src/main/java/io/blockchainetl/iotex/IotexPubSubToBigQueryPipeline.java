package io.blockchainetl.iotex;

import com.google.common.collect.Lists;
import io.blockchainetl.common.PubSubToBigQueryPipelineOptions;
import io.blockchainetl.common.domain.ChainConfig;
import io.blockchainetl.iotex.fns.EntityJsonToTableRow;
import org.apache.beam.sdk.Pipeline;
import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO;
import org.apache.beam.sdk.io.gcp.bigquery.InsertRetryPolicy;
import org.apache.beam.sdk.io.gcp.bigquery.WriteResult;
import org.apache.beam.sdk.io.gcp.pubsub.PubsubIO;
import org.apache.beam.sdk.options.PipelineOptionsFactory;

import java.util.List;

import static io.blockchainetl.common.PubSubToBigQueryPipeline.readChainConfigs;


public class IotexPubSubToBigQueryPipeline {

    private static final String PUBSUB_ID_ATTRIBUTE = "item_id";

    public static void main(String[] args) {
        PubSubToBigQueryPipelineOptions options =
            PipelineOptionsFactory.fromArgs(args).withValidation().as(PubSubToBigQueryPipelineOptions.class);
        
        Pipeline pipeline = Pipeline.create(options);
        
        List<ChainConfig> chainConfigs = readChainConfigs(options.getChainConfigFile());

        List<String> entityNames = Lists.newArrayList("blocks", "actions", "logs", "evm_transfers");
        
        for (ChainConfig chainConfig : chainConfigs) {
            for (String entityName : entityNames) {
                buildPipelineForEntity(pipeline, chainConfig, entityName);
            }
        }

        pipeline.run();
    }

    private static void buildPipelineForEntity(Pipeline pipeline, ChainConfig chainConfig, String entityName) {
        String subscriptionName = chainConfig.getPubSubSubscriptionPrefix() + "." + entityName;
        String tableName = chainConfig.getBigQueryDataset() + "." + entityName;
        String transformNamePrefix = chainConfig.getTransformNamePrefix();

        WriteResult writeResult = pipeline
            .apply(transformNamePrefix + "PubSubListener", PubsubIO.readStrings()
                .fromSubscription(subscriptionName)
                .withIdAttribute(PUBSUB_ID_ATTRIBUTE))
            .apply(transformNamePrefix + "WriteToBigQuery", BigQueryIO.<String>write()
                .to(tableName)
                .withFormatFunction(new EntityJsonToTableRow())
                .ignoreUnknownValues()
                .withCreateDisposition(BigQueryIO.Write.CreateDisposition.CREATE_NEVER)
                .withWriteDisposition(BigQueryIO.Write.WriteDisposition.WRITE_APPEND)
                .withoutValidation()
                .withExtendedErrorInfo()
                .withMethod(BigQueryIO.Write.Method.STREAMING_INSERTS)
                .withFailedInsertRetryPolicy(InsertRetryPolicy.retryTransientErrors()));
    }
}
