SELECT 
    "Customer ID"
	,Age
	,Gender
	,"Item Purchased"
	,Category
	,"Purchase Amount (USD)"
	,Location
	,Size
	,Color
	,Season
	,"Review Rating"
	,"Subscription Status"
	,"Shipping Type"
	,"Discount Applied"
	,"Promo Code Used"
	,"Previous Purchases"
	,"Payment Method"
	,"Frequency of Purchases"
FROM {{ source('ecommerce_raw', 'customer_details') }}