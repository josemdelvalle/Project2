drop table user_credentials ;
create table user_credentials(
	user_id    serial  primary key not null,
	username   varchar(50) unique not null,
	password_  varchar(50) not null,
	customer_id serial REFERENCES customers(customer_id) ON DELETE cascade 
	
);


drop table  customers ;
create table customers(
	customer_id   serial    primary key not null,
	first_name    varchar(50) not null,
	last_name     varchar(50) not null,
	phone_number  varchar(50),
	email         varchar(50)
);



drop table products ;
create table products(
	product_id serial primary key not null,
	flavor        varchar(50) not null,
	topping1      varchar(50),
	topping2      varchar(50),
	topping3      varchar(50),
	topping4      varchar(50),
	topping5      varchar(50),
	-- Cup or Cone
	holder_type   varchar(50) not null,
	-- Medium, Large, or Small
	holder_size   varchar(50) not null,
	product_price  decimal(5,2) not null
	
);

drop table orders ;
create table orders(
	order_id serial primary key not null,
	order_number bigint not null,
	quantity int not null,
	product_id serial REFERENCES products(product_id) ON DELETE cascade 	
	
);


insert into public.customers values(
--default,  'serene', 'samb', '913-453-5334', 'samb@gmail.com'
default,  'jose',   'del', '343-434-5356', 'del@gmail.com'
);

insert into public.user_credentials values(
default,  'serene', '12345'
);


/*select * from public.customers ;
join user_credentials uc on c.customer_id = uc.customer_id ;

insert into public.user_credentials values(
default,  'jose', '12345'
);

select * from user_credentials where username = 'serene' and password_ = '12345';
select * from customers c2 ;
*/

