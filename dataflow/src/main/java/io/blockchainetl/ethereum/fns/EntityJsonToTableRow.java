package io.blockchainetl.ethereum.fns;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.google.api.services.bigquery.model.TableRow;
import org.apache.beam.sdk.transforms.SerializableFunction;
import org.slf4j.Logger;


/*-
 * ‌
 * Hedera ETL
 * ​
 * Copyright (C) 2020 Hedera Hashgraph, LLC
 * ​
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * ‍
 */

/**
 * Converts Hedera transaction json string to TableRow.
 * Uses transaction's consensusTimestamp too add an extra field - consensusTimestampTruncated.
 */
public class EntityJsonToTableRow implements SerializableFunction<String, TableRow> {

    private static final Logger LOG = org.slf4j.LoggerFactory.getLogger(EntityJsonToTableRow.class);
    private static final ObjectMapper MAPPER = new ObjectMapper();

    @Override
    public TableRow apply(String json) {
        try {
            TableRow tableRow = MAPPER.readValue(json, TableRow.class);
            LOG.trace("Table Row: {}", tableRow.toPrettyString());
            return tableRow;
        } catch (Exception e) {
            LOG.error("Error converting json to TableRow. Json: " + json, e);
            throw new IllegalArgumentException("Error converting json to TableRow", e);
        }
    }
}
