package io.blockchainetl.common;

import org.apache.beam.sdk.options.Description;
import org.apache.beam.sdk.options.PipelineOptions;
import org.apache.beam.sdk.options.SdkHarnessOptions;
import org.apache.beam.sdk.options.StreamingOptions;
import org.apache.beam.sdk.options.Validation;

public interface PubSubToBigQueryPipelineOptions extends PipelineOptions, StreamingOptions, SdkHarnessOptions {
    
    @Description("JSON file containing chain configuration")
    @Validation.Required
    String getChainConfigFile();

    void setChainConfigFile(String value);

    @Description("Timestamp skew for blocks and transactions, messages older than this will be rejected")
    Long getAllowedTimestampSkewSeconds();

    void setAllowedTimestampSkewSeconds(Long allowedTimestampSkewSeconds);

    @Description("The Cloud Pub/Sub subscription to consume from. The name should be in the format of " +
        "projects/<project-id>/subscriptions/<subscription-name>.")
    org.apache.beam.sdk.options.ValueProvider<String> getInputSubscription();
    void setInputSubscription(org.apache.beam.sdk.options.ValueProvider<String> value);

    @Description("BigQuery table to output transactions to. The name should be in the format of " +
        "<project-id>:<dataset-id>.<table-name>.")
    org.apache.beam.sdk.options.ValueProvider<String> getOutputTransactionsTable();
    void setOutputTransactionsTable(org.apache.beam.sdk.options.ValueProvider<String> value);

    @Description("BigQuery table to output errors to. The name should be in the format of " +
        "<project-id>:<dataset-id>.<table-name>.")
    org.apache.beam.sdk.options.ValueProvider<String> getOutputErrorsTable();
    void setOutputErrorsTable(org.apache.beam.sdk.options.ValueProvider<String> value);
}
