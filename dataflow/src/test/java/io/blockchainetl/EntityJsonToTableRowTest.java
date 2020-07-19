package io.blockchainetl;

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

import io.blockchainetl.ethereum.fns.EntityJsonToTableRow;
import org.junit.Test;

import java.nio.file.Files;
import java.util.List;
import java.io.IOException;

import static org.junit.jupiter.api.Assertions.assertLinesMatch;

public class EntityJsonToTableRowTest {
    private final EntityJsonToTableRow converter = new EntityJsonToTableRow();

    @Test
    public void testConversion() throws Exception {
        // Given
        List<String> jsonTransactions = readFileLines("testdata/TransactionJsonToTableRowTest/blocks.txt");
        List<String> expected = readFileLines("testdata/TransactionJsonToTableRowTest/expectedBlocks.txt");

        // when
        List<String> actual = jsonTransactions.stream()
                .map(converter::apply)
                .map(com.google.api.services.bigquery.model.TableRow::toString)
                .collect(java.util.stream.Collectors.toList());

        // then
        assertLinesMatch(expected, actual);
    }

    private List<String> readFileLines(String fileName) throws IOException {
        return Files.readAllLines(java.nio.file.Paths.get(this.getClass().getClassLoader().getResource(fileName).getPath()));
    }
}
