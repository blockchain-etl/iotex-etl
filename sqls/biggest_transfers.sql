#standardSQL
SELECT `hash`, timestamp, height, sender, transfer
FROM `public-data-finance.crypto_iotex.actions`
WHERE status = 1 AND action_type = 'transfer'
ORDER BY transfer.amount DESC
LIMIT 1000