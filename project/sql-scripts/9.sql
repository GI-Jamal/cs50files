SELECT SUM(C.quantity) as Quantity FROM cart AS C JOIN products AS P ON C.product_id = P.product_id WHERE user_id = ? GROUP BY user_id;


INSERT INTO TABLE orders (order_date, user_id, item_count, cost) VALUES (?, ?, ?, ?);


SELECT order_id from orders ORDER BY order_id DESC LIMIT 1;

WITH temptable AS
(SELECT P.product_id AS Product, SUM(C.quantity) as Quantity, P.price AS PricePerUnit, SUM(C.quantity * P.price) AS Subtotal FROM cart AS C JOIN products AS P ON C.product_id = P.product_id WHERE user_id = ? GROUP BY C.product_id, C.quantity)
INSERT INTO order_info (order_id, product_id, quantity, priceperunit)
SELECT ?, Product, Quantity, PricePerUnit
FROM temptable;


