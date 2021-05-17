drop table if exists product_cart;

CREATE TABLE product_cart(user_id serial primary key references users(user_id), 
product_id serial REFERENCES products(product_id), product_name varchar(50), 
product_price decimal(5,2), quantity smallint);

drop table if exists orders_;

create table orders_(order_id serial primary key not null,
	order_number bigint not null,
	quantity int not null,
	product_id serial REFERENCES products(product_id) ON DELETE cascade, 	
	user_id serial references users(user_id)
);