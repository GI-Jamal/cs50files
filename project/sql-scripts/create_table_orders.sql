CREATE TABLE IF NOT EXISTS "orders" (
    order_id INTEGER PRIMARY KEY NOT NULL,
    order_date DATETIME NOT NULL,
    user_id INTEGER NULL,
    item_count INTEGER NOT NULL,
    total FLOAT NOT NULL
);