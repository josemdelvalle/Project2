drop table if exists product_cart;

CREATE TABLE product_cart(user_id serial primary key references users(user_id), 
product_id serial REFERENCES products(product_id), product_name varchar(50), 
product_price decimal(5,2), quantity smallint);