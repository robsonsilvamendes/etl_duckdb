SELECT 
    "Uniqe Id"
	,"Product Name"
	,"Brand Name"
	,Asin
	,Category
	,"Upc Ean Code"
	,"List Price"
	,"Selling Price"
	,Quantity
	,"Model Number"
	,"About Product"
	,"Product specification"
	,"Technical Details"
	,"Shipping Weight"
	,"Product Dimensions"
	,image
	,Variants
	,Sku
	,"Product Url"
	,Stock
	,"Product Details"
	,Dimensions
	,Color
	,Ingredients
	,"Direction To Use"
	,"Is Amazon Seller"
	,"Size Quantity Variant"
	,"Product Description"
FROM {{ source('ecommerce_raw', 'product_details') }}