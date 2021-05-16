drop table if exists product_cart;

CREATE TABLE product_cart(product_id serial primary key REFERENCES products(
product_id), product_name varchar(50), product_price decimal(5,2));