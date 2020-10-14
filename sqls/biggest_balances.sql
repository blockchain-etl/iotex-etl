#standardSQL
WITH double_entry_book as (
    -- transaction logs debits
    SELECT recipient as address, amount AS value
    FROM `public-data-finance.crypto_iotex.transaction_logs` AS transaction_logs
    UNION ALL
    -- transaction logs credits
    SELECT sender as address, -amount AS value
    FROM `public-data-finance.crypto_iotex.transaction_logs` AS transaction_logs
    UNION ALL
    -- initial balances debits
    SELECT address as address, balance AS value
    FROM `public-data-finance.crypto_iotex.initial_balances`
)
SELECT address, SUM(value) AS balance
FROM double_entry_book
GROUP BY address
ORDER BY balance DESC
LIMIT 1000