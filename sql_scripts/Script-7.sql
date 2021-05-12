create table user_credentials(
	user_id    serial  primary key not null,
	username   varchar(50) unique not null,
	password_  varchar(50) not null,
	is_admin   bool,
	customer_id serial REFERENCES customers(customer_id) ON DELETE cascade 
	
);


create table customers(
	customer_id   serial    primary key not null,
	first_name    varchar(50) not null,
	last_name     varchar(50) not null,
	phone_number  varchar(50),
	email         varchar(50)
);

create table products(
	product_id serial primary key not null,
	product_name  varchar(50), not null,
	product_price  decimal(5,2) not null
)

create table orders(
	order_id serial primary key not null,
	
	

)