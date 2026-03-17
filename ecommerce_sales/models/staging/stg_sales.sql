SELECT 
    "user id"
	,"product id"
	,"interaction type"
	,"Time stamp"
	,column4
FROM {{ source('ecommerce_raw', 'ecommerece_sales_data_2024') }}