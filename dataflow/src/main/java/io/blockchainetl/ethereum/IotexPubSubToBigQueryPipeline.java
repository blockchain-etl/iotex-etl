package io.blockchainetl.ethereum;

import io.blockchainetl.common.PubSubToBigQueryPipelineOptions;
import io.blockchainetl.ethereum.fns.EntityJsonToTableRow;
import org.apache.beam.sdk.Pipeline;
import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO;
import org.apache.beam.sdk.io.gcp.bigquery.InsertRetryPolicy;
import org.apache.beam.sdk.io.gcp.bigquery.WriteResult;
import org.apache.beam.sdk.io.gcp.pubsub.PubsubIO;
import org.apache.beam.sdk.options.PipelineOptionsFactory;


public class IotexPubSubToBigQueryPipeline {

    public static void main(String[] args) {
        PubSubToBigQueryPipelineOptions options =
            PipelineOptionsFactory.fromArgs(args).withValidation().as(PubSubToBigQueryPipelineOptions.class);

        
        Pipeline pipeline = Pipeline.create(options);
        
        for (String table : com.google.common.collect.Lists.newArrayList("blocks", "actions"))
        WriteResult writeResult = pipeline
            .apply("PubSubListener", PubsubIO.readStrings()
                .fromSubscription(options.getInputSubscription())
                .withIdAttribute("consensusTimestamp"))
            .apply("WriteToBigQuery", BigQueryIO.<String>write()
                .to(options.getOutputTransactionsTable())
                .withFormatFunction(new EntityJsonToTableRow())
                .ignoreUnknownValues()
                .withCreateDisposition(BigQueryIO.Write.CreateDisposition.CREATE_NEVER)
                .withWriteDisposition(BigQueryIO.Write.WriteDisposition.WRITE_APPEND)
                .withoutValidation()
                .withExtendedErrorInfo()
                .withMethod(BigQueryIO.Write.Method.STREAMING_INSERTS)
                .withFailedInsertRetryPolicy(InsertRetryPolicy.retryTransientErrors()));
        pipeline.run();
    }
}
