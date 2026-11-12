CREATE DATABASE olist_ecommerce;
USE olist_ecommerce;
SHOW TABLES;
SELECT COUNT(*)
FROM olist_ecommerce.olist_customers_dataset;

SHOW VARIABLES LIKE 'local_infile';
USE olist_ecommerce;
TRUNCATE TABLE olist_geolocation_dataset;
LOAD DATA LOCAL INFILE
'C:/Excel/DA1/project 4/Advanced_Ecommerce_Analytics/Dataset/Raw/olist_geolocation_dataset.csv'
INTO TABLE olist_geolocation_dataset
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(
    geolocation_zip_code_prefix,
    geolocation_lat,
    geolocation_lng,
    geolocation_city,
    geolocation_state
);
SHOW WARNINGS;
USE olist_ecommerce;

TRUNCATE TABLE olist_geolocation_dataset;

LOAD DATA LOCAL INFILE
'C:/Excel/DA1/project 4/Advanced_Ecommerce_Analytics/Dataset/Raw/olist_geolocation_dataset.csv'
INTO TABLE olist_geolocation_dataset
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
    geolocation_zip_code_prefix,
    geolocation_lat,
    geolocation_lng,
    geolocation_city,
    geolocation_state
);
USE olist_ecommerce;

SELECT COUNT(*) AS Total_Rows
FROM olist_geolocation_dataset;
USE olist_ecommerce;

SHOW TABLES;
USE olist_ecommerce;

CREATE TABLE olist_order_items_dataset (
    order_id VARCHAR(32),
    order_item_id INT,
    product_id VARCHAR(32),
    seller_id VARCHAR(32),
    shipping_limit_date DATETIME,
    price DECIMAL(10,2),
    freight_value DECIMAL(10,2)
);
USE olist_ecommerce;

LOAD DATA LOCAL INFILE
'C:/Excel/DA1/project 4/Advanced_Ecommerce_Analytics/Dataset/Raw/olist_order_items_dataset.csv'
INTO TABLE olist_order_items_dataset
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
    order_id,
    order_item_id,
    product_id,
    seller_id,
    shipping_limit_date,
    price,
    freight_value
);
SELECT COUNT(*) AS Total_Rows
FROM olist_order_items_dataset;
USE olist_ecommerce;

CREATE TABLE olist_order_payments_dataset (
    order_id VARCHAR(32),
    payment_sequential INT,
    payment_type VARCHAR(50),
    payment_installments INT,
    payment_value DECIMAL(10,2)
);
USE olist_ecommerce;

LOAD DATA LOCAL INFILE
'C:/Excel/DA1/project 4/Advanced_Ecommerce_Analytics/Dataset/Raw/olist_order_payments_dataset.csv'
INTO TABLE olist_order_payments_dataset
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
    order_id,
    payment_sequential,
    payment_type,
    payment_installments,
    payment_value
);
SELECT COUNT(*) AS Total_Rows
FROM olist_order_payments_dataset;
CREATE TABLE olist_order_reviews_dataset (
    review_id VARCHAR(32),
    order_id VARCHAR(32),
    review_score INT,
    review_comment_title TEXT,
    review_comment_message TEXT,
    review_creation_date DATETIME,
    review_answer_timestamp DATETIME
);
LOAD DATA LOCAL INFILE
'C:/Excel/DA1/project 4/Advanced_Ecommerce_Analytics/Dataset/Raw/olist_order_reviews_dataset.csv'
INTO TABLE olist_order_reviews_dataset
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
    review_id,
    order_id,
    review_score,
    review_comment_title,
    review_comment_message,
    review_creation_date,
    review_answer_timestamp
);
SELECT COUNT(*) AS Total_Rows
FROM olist_order_reviews_dataset;

SHOW WARNINGS;
SELECT COUNT(*) AS Total_Rows
FROM olist_order_reviews_dataset;
CREATE TABLE olist_orders_dataset (
    order_id VARCHAR(32),
    customer_id VARCHAR(32),
    order_status VARCHAR(30),
    order_purchase_timestamp DATETIME,
    order_approved_at DATETIME,
    order_delivered_carrier_date DATETIME,
    order_delivered_customer_date DATETIME,
    order_estimated_delivery_date DATETIME
);
LOAD DATA LOCAL INFILE
'C:/Excel/DA1/project 4/Advanced_Ecommerce_Analytics/Dataset/Raw/olist_orders_dataset.csv'
INTO TABLE olist_orders_dataset
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
    order_id,
    customer_id,
    order_status,
    order_purchase_timestamp,
    order_approved_at,
    order_delivered_carrier_date,
    order_delivered_customer_date,
    order_estimated_delivery_date
);
SHOW WARNINGS;
TRUNCATE TABLE olist_orders_dataset;
LOAD DATA LOCAL INFILE
'C:/Excel/DA1/project 4/Advanced_Ecommerce_Analytics/Dataset/Raw/olist_orders_dataset.csv'
INTO TABLE olist_orders_dataset
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
    order_id,
    customer_id,
    order_status,
    @purchase,
    @approved,
    @carrier,
    @delivered,
    @estimated
)
SET
    order_purchase_timestamp = NULLIF(@purchase, ''),
    order_approved_at = NULLIF(@approved, ''),
    order_delivered_carrier_date = NULLIF(@carrier, ''),
    order_delivered_customer_date = NULLIF(@delivered, ''),
    order_estimated_delivery_date = NULLIF(@estimated, '');
SELECT COUNT(*) AS Total_Rows
FROM olist_orders_dataset;
CREATE TABLE olist_products_dataset (
    product_id VARCHAR(32),
    product_category_name VARCHAR(100),
    product_name_lenght INT,
    product_description_lenght INT,
    product_photos_qty INT,
    product_weight_g INT,
    product_length_cm INT,
    product_height_cm INT,
    product_width_cm INT
);
LOAD DATA LOCAL INFILE
'C:/Excel/DA1/project 4/Advanced_Ecommerce_Analytics/Dataset/Raw/olist_products_dataset.csv'
INTO TABLE olist_products_dataset
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
    product_id,
    product_category_name,
    product_name_lenght,
    product_description_lenght,
    product_photos_qty,
    product_weight_g,
    product_length_cm,
    product_height_cm,
    product_width_cm
);
SHOW WARNINGS;
TRUNCATE TABLE olist_products_dataset;
LOAD DATA LOCAL INFILE
'C:/Excel/DA1/project 4/Advanced_Ecommerce_Analytics/Dataset/Raw/olist_products_dataset.csv'
INTO TABLE olist_products_dataset
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
    product_id,
    product_category_name,
    @name_length,
    @description_length,
    @photos_qty,
    @weight,
    @length,
    @height,
    @width
)
SET
    product_name_lenght = NULLIF(@name_length, ''),
    product_description_lenght = NULLIF(@description_length, ''),
    product_photos_qty = NULLIF(@photos_qty, ''),
    product_weight_g = NULLIF(@weight, ''),
    product_length_cm = NULLIF(@length, ''),
    product_height_cm = NULLIF(@height, ''),
    product_width_cm = NULLIF(@width, '');
SELECT COUNT(*) AS Total_Rows
FROM olist_products_dataset;
CREATE TABLE olist_sellers_dataset (
    seller_id VARCHAR(32),
    seller_zip_code_prefix INT,
    seller_city VARCHAR(100),
    seller_state VARCHAR(10)
);
LOAD DATA LOCAL INFILE
'C:/Excel/DA1/project 4/Advanced_Ecommerce_Analytics/Dataset/Raw/olist_sellers_dataset.csv'
INTO TABLE olist_sellers_dataset
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
    seller_id,
    seller_zip_code_prefix,
    seller_city,
    seller_state
);
SELECT COUNT(*) AS Total_Rows
FROM olist_sellers_dataset;
CREATE TABLE product_category_name_translation (
    product_category_name VARCHAR(100),
    product_category_name_english VARCHAR(100)
);
LOAD DATA LOCAL INFILE
'C:/Excel/DA1/project 4/Advanced_Ecommerce_Analytics/Dataset/Raw/product_category_name_translation.csv'
INTO TABLE product_category_name_translation
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
    product_category_name,
    product_category_name_english
);
USE olist_ecommerce;

SELECT 'customers' AS Table_Name, COUNT(*) AS Total_Rows
FROM olist_customers_dataset

UNION ALL

SELECT 'geolocation', COUNT(*)
FROM olist_geolocation_dataset

UNION ALL

SELECT 'order_items', COUNT(*)
FROM olist_order_items_dataset

UNION ALL

SELECT 'order_payments', COUNT(*)
FROM olist_order_payments_dataset

UNION ALL

SELECT 'order_reviews', COUNT(*)
FROM olist_order_reviews_dataset

UNION ALL

SELECT 'orders', COUNT(*)
FROM olist_orders_dataset

UNION ALL

SELECT 'products', COUNT(*)
FROM olist_products_dataset

UNION ALL

SELECT 'sellers', COUNT(*)
FROM olist_sellers_dataset

UNION ALL

SELECT 'category_translation', COUNT(*)
FROM product_category_name_translation;
SHOW TABLES;
SELECT
    COUNT(DISTINCT order_id) AS Total_Orders,
    ROUND(SUM(price), 2) AS Total_Revenue,
    ROUND(AVG(price), 2) AS Average_Order_Value
FROM olist_order_items_dataset;
SELECT
    DATE_FORMAT(o.order_purchase_timestamp, '%Y-%m') AS Month,
    COUNT(DISTINCT o.order_id) AS Total_Orders,
    ROUND(SUM(oi.price), 2) AS Monthly_Revenue
FROM olist_orders_dataset o
JOIN olist_order_items_dataset oi
    ON o.order_id = oi.order_id
GROUP BY Month
ORDER BY Month;
SELECT
    COALESCE(t.product_category_name_english, 'Unknown') AS Category,
    COUNT(DISTINCT oi.order_id) AS Total_Orders,
    ROUND(SUM(oi.price), 2) AS Total_Revenue
FROM olist_order_items_dataset oi
JOIN olist_products_dataset p
    ON oi.product_id = p.product_id
LEFT JOIN product_category_name_translation t
    ON p.product_category_name = t.product_category_name
GROUP BY Category
ORDER BY Total_Revenue DESC
LIMIT 10;
SELECT
    payment_type,
    COUNT(*) AS Total_Transactions,
    ROUND(SUM(payment_value), 2) AS Total_Payment,
    ROUND(AVG(payment_value), 2) AS Average_Payment
FROM olist_order_payments_dataset
GROUP BY payment_type
ORDER BY Total_Payment DESC;
SELECT
    c.customer_state,
    COUNT(DISTINCT o.order_id) AS Total_Orders,
    ROUND(SUM(oi.price), 2) AS Total_Revenue
FROM olist_customers_dataset c
JOIN olist_orders_dataset o
    ON c.customer_id = o.customer_id
JOIN olist_order_items_dataset oi
    ON o.order_id = oi.order_id
GROUP BY c.customer_state
ORDER BY Total_Revenue DESC
LIMIT 10;
SELECT
    order_status,
    COUNT(*) AS Total_Orders,
    ROUND(
        COUNT(*) * 100.0 / (SELECT COUNT(*) FROM olist_orders_dataset),
        2
    ) AS Order_Percentage
FROM olist_orders_dataset
GROUP BY order_status
ORDER BY Total_Orders DESC;
SELECT
    s.seller_id,
    s.seller_state,
    COUNT(DISTINCT oi.order_id) AS Total_Orders,
    ROUND(SUM(oi.price), 2) AS Total_Revenue
FROM olist_sellers_dataset s
JOIN olist_order_items_dataset oi
    ON s.seller_id = oi.seller_id
GROUP BY s.seller_id, s.seller_state
ORDER BY Total_Revenue DESC
LIMIT 10;
SELECT
    ROUND(
        AVG(
            DATEDIFF(
                order_delivered_customer_date,
                order_purchase_timestamp
            )
        ), 2
    ) AS Average_Delivery_Days,

    MIN(
        DATEDIFF(
            order_delivered_customer_date,
            order_purchase_timestamp
        )
    ) AS Minimum_Delivery_Days,

    MAX(
        DATEDIFF(
            order_delivered_customer_date,
            order_purchase_timestamp
        )
    ) AS Maximum_Delivery_Days

FROM olist_orders_dataset
WHERE order_status = 'delivered';
SELECT
    review_score,
    COUNT(*) AS Total_Reviews,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM olist_order_reviews_dataset),
        2
    ) AS Review_Percentage
FROM olist_order_reviews_dataset
GROUP BY review_score
ORDER BY review_score DESC;
SELECT
    ROUND(SUM(price), 2) AS Total_Product_Revenue,
    ROUND(SUM(freight_value), 2) AS Total_Freight_Cost,
    ROUND(AVG(freight_value), 2) AS Average_Freight_Cost,
    ROUND(
        SUM(freight_value) * 100.0 / SUM(price), 2
    ) AS Freight_Percentage
FROM olist_order_items_dataset;