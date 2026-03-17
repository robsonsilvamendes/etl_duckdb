WITH sales AS (
    SELECT * FROM {{ ref('stg_sales') }}

), product_details AS (
    SELECT * FROM {{ ref('stg_product_details') }}

), customer_details AS (
    SELECT * FROM {{ ref('stg_customer_details') }}
)

SELECT 
	pd."Product Name"
	,pd."Category"
	,c.Age
	,c.Gender
	,c."Item Purchased"
	,s.*
FROM ecommerece_sales_data_2024 s
LEFT JOIN product_details pd ON s."product id" = pd."Uniqe Id"
LEFT JOIN customer_details c ON c."Customer ID" = s."user id"