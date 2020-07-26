package io.blockchainetl;

import io.blockchainetl.iotex.fns.EntityJsonToTableRow;
import org.junit.Test;

import java.io.IOException;
import java.nio.file.Files;
import java.util.List;

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
        return Files.readAllLines(
            java.nio.file.Paths.get(this.getClass().getClassLoader().getResource(fileName).getPath()));
    }
}
