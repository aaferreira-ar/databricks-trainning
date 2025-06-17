-- Please edit the sample below

CREATE OR REPLACE MATERIALIZED VIEW sales_resume AS
SELECT
    c.city,
    sum(s.value) as value
FROM LIVE.sales as s
LEFT JOIN LIVE.customers as c
ON s.customer_id = c.customer_id
group by all