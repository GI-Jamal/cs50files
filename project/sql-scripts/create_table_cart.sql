CREATE TABLE IF NOT EXISTS "cart" (
    cart_item_id INTEGER PRIMARY KEY NOT NULL,
    user_id INTEGER NULL,
    quantity INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    FOREIGN KEY(product_id) REFERENCES products(product_id)
);