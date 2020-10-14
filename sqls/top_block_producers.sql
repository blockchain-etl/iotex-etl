#standardSQL
SELECT producer, COUNT(*) AS block_count
FROM `public-data-finance.crypto_iotex.blocks`
GROUP BY producer
ORDER BY block_count DESC
LIMIT 1000