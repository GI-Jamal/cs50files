SELECT P.product_id AS Product, SUM(C.quantity) as Quantity, P.price AS PricePerUnit, SUM(C.quantity * P.price) AS Subtotal FROM cart AS C JOIN products AS P ON C.product_id = P.product_id WHERE user_id = 1 GROUP BY C.product_id, C.quantity;


WITH totalcost AS (SELECT  SUM(C.quantity * P.price) AS Subtotal FROM cart AS C JOIN products AS P ON C.product_id = P.product_id WHERE user_id = 1 GROUP BY C.product_id, C.quantity) SELECT SUM(Subtotal) AS Total FROM totalcost;

