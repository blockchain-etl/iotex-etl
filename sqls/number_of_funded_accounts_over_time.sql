#standardSQL
-- Read this article to understand this query https://medium.com/google-cloud/plotting-ethereum-address-growth-chart-55cc0e7207b2
WITH double_entry_book as (
    -- transaction logs debits
    SELECT timestamp, recipient as address, amount AS value
    FROM `public-data-finance.crypto_iotex.transaction_logs` AS transaction_logs
    UNION ALL
    -- transaction logs credits
    SELECT timestamp, transaction_logs.sender as address, -amount AS value
    FROM `public-data-finance.crypto_iotex.transaction_logs` AS transaction_logs
    UNION ALL
    -- initial balances debits, timestamp of block 1
    SELECT '2019-04-22 02:06:30', address as address, balance AS value
    FROM `public-data-finance.crypto_iotex.initial_balances`
),
double_entry_book_grouped_by_date as (
    SELECT address, sum(value) AS balance_increment, DATE(timestamp) AS date
    FROM double_entry_book
    GROUP BY address, date
),
daily_balances_with_gaps AS (
    SELECT address, date, SUM(balance_increment) OVER (PARTITION BY address ORDER BY date) AS balance,
    LEAD(date, 1, CURRENT_DATE()) OVER (PARTITION BY address ORDER BY date) AS next_date
    FROM double_entry_book_grouped_by_date
),
calendar AS (
    SELECT date FROM UNNEST(GENERATE_DATE_ARRAY('2019-04-22', CURRENT_DATE())) AS date
),
daily_balances AS (
    SELECT address, calendar.date, balance
    FROM daily_balances_with_gaps
    JOIN calendar ON daily_balances_with_gaps.date <= calendar.date AND calendar.date < daily_balances_with_gaps.next_date
)
SELECT date, COUNT(*) AS address_count
FROM daily_balances
WHERE balance > 0
GROUP BY date
ORDER BY date DESC
