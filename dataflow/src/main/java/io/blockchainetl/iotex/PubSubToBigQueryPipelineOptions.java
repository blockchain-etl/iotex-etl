package io.blockchainetl.iotex;

import org.apache.beam.sdk.options.Description;
import org.apache.beam.sdk.options.PipelineOptions;
import org.apache.beam.sdk.options.StreamingOptions;
import org.apache.beam.sdk.options.Validation;
import org.apache.beam.sdk.options.ValueProvider;

public interface PubSubToBigQueryPipelineOptions extends PipelineOptions, StreamingOptions {

    @Description("The transform name prefix")
    @Validation.Required
    String getTransformNamePrefix();

    void setTransformNamePrefix(String value);

    @Description("The prefix of PubSub subscription")
    @Validation.Required
    ValueProvider<String> getPubSubSubscriptionPrefix();

    void setPubSubSubscriptionPrefix(ValueProvider<String> value);

    @Description("The BigQuery dataset name")
    @Validation.Required
    ValueProvider<String> getBigQueryDataset();

    void setBigQueryDataset(ValueProvider<String> value);

    @Description("BigQuery table to output errors to. The name should be in the format of " +
        "<project-id>:<dataset-id>.<table-name>.")
    ValueProvider<String> getOutputErrorsTable();
    void setOutputErrorsTable(ValueProvider<String> value);
}
