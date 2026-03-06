Create database PracticeSql;
use PracticeSql;
-- creating first table 
create table employees(
	employee_id int,
    first_name varchar(50),
    last_name varchar(50),
    email varchar(50),
    hourly_pay decimal(10,2),
    date datetime
);

-- change data type 
alter table employees
modify date date;

-- change column name 
alter table employees 
change date hire_date date;


-- inserting data into table 
insert into employees
values 	(1, "Ayush", "Harduth", "ayush.har27@gmail.com", 129000.34, '2026-02-12'),
		(2, "Squidward", "Tentacles", "Squidward.Tentacles@gmail.com", 129.34, '2026-02-13'),
		(3, "Eugene", "Krabs", "Eugene.Krabs@gmail.com", 234.34, '2026-02-14'),
		(4, "Spongebob", "Squarepants", "Spongebob.Squarepants@gmail.com", 5869.58, '2026-02-15'),
		(5, "Patric", "Star", "Patric.Star@gmail.com", 2948.06, '2026-02-16');

-- displaying the table 
select * from employees;

-- turning safe updates off to delete rows 
set sql_safe_updates =0;

-- deleting according to employee id
delete from employees 
where employee_id = 1;

-- turning it back on so i dont acciedently delete something i done want to 
set sql_safe_updates =1;  

-- where 
select * from employees 
where employee_id = 2;

select * from employees 
where hourly_pay >= 100;

select * from employees
where employee_id != 1;

-- adding a row with missing values 

insert into employees(employee_id, first_name, last_name, email)
values 	(6, "Sheldon", "Plankton", "Sheldon.Plankton@gmail.com");
select * from employees;

select *
from employees
where hourly_pay is null;

-- update and delete from a table 

set sql_safe_updates =0;
update employees 
set hourly_pay = 37484.89,
	hire_date = "2026-02-17"
where employee_id = 6;
select * from employees;


set autocommit = off;
-- create a save point 
commit;

-- rollback 
rollback;

-- unique constriant 
-- it means we cant add any new product names that are the same 
create table products(
	product_id int,
    product_name varchar(50),
    product_price decimal(4,2)

);

-- add unique if u forget to add it 
alter table products add constraint unique(product_name);

-- add values 
insert into products
values 	(100, "hamburger", 3.99),
		(101, "fries", 1.89),
		(102, "soda", 1.00),
		(103, "ice-cream", 1.75);

-- when creating a table adding constraints adds data validation to the table 
alter table products modify product_price decimal(4,2) not null;


-- check constraint 
-- the check constraint checks if the values in the table match the arguement in the check 
-- so if i tried to add a product witha rice lower than 1.00 then it would throw a error 
-- i didnt run this but just showing how it works 
create table products(
	product_id int,
    product_name varchar(50),
    product_price decimal(4,2),
    constraint minimum_price check(product_price > 1.00)
);

-- adding a check constriant to a table that already excists 
alter table products 
add constraint minimum_price check(product_price >= 1.00);

-- drop a check 
alter table products 
drop check minimum_price;

-- defualt constraint 
-- adds a defulat value if the values is null 
insert into products 
values	(105,"straw", 0.00),
		(106,"napkin", 0.00),
		(107,"fork", 0.00),
        (108,"spoon", 0.00);
commit; 

delete from products where product_id >= 104;

select * from products;

alter table products 
alter product_price set default 0; 

insert into products (product_id, product_name)
values	(105,"straw"),
		(106,"napkin"),
		(107,"fork"),
        (108,"spoon");

commit;
-- primary key 
-- unique value 

create table transactions(
	transaction_id int primary key,
    amount decimal(4,2)
);

alter table transactions
modify column amount decimal(4,2);

-- adding a primary key 
-- can only have 1 primary key per table 
alter table transactions
add constraint 
primary key(transaction_id);

insert into transactions
values(101, 4.33);
select * from transactions;

drop table transactions;


-- auto increment ]
create table transactions(
	transaction_id int primary key auto_increment,
    amount decimal(4,2)
);

select * from transactions;

insert into transactions(amount)
values(6.68);

alter table transactions 
auto_increment= 1000;

delete from transactions;
drop table transactions;

insert into transactions(amount)
values(48.89);

commit;
-- foregin keys 
-- links tables using there primary keys 
create table customers(
	customer_id int primary key auto_increment,
    first_name varchar(50),
    last_name varchar(50)
);

insert into customers(first_name, last_name)
values
("Fred","Fish"),
("Larry", "Lobster"),
("Bubble", "Bass")
;
select * from customers;


drop table transactions;

-- foreign keys 

create table transactions(
	transaction_id int primary key auto_increment,
    amount decimal(5,2),
    customer_id int,
    foreign key(customer_id) references customers(customer_id)
);
select * from transactions;

alter table transactions 
add constraint fk_customer_id -- gives it a name 
foreign key(customer_id) references customers(customer_id);

set sql_safe_updates =0;
delete from transactions;
select * from transactions;

alter table transactions 
auto_increment = 1000;

insert into transactions(amount, customer_id)
values
(4.99,3),
(2.89,2),
(3.38,3),
(2.89,1)
;

-- joins 

insert into transactions(amount, customer_id)
values
(1.00, NULL);
select * from transactions;

insert into customers(first_name, last_name)
values
("Poppy", "Puff");
select * from customers;


-- inner, left outer joins 
select *
from 
transactions 
inner join customers
on transactions.customer_id = customers.customer_id;

-- so it excluded the records that dont have matching customer_ids accross both tables 

select first_name, last_name, transaction_id, amount
from 
transactions 
inner join customers
on transactions.customer_id = customers.customer_id;

-- left join
-- displays the joint table regardless of missing data 
select *
from 
transactions 
left join customers
on transactions.customer_id = customers.customer_id;

-- right join 
-- display the table on the right and display all data regardless of missing data 
select *
from 
transactions 
right join customers
on transactions.customer_id = customers.customer_id;

-- functions 
-- count 
select count(amount) as todays_transactions
from transactions;

-- max
select max(amount) as maximum 
from transactions;

-- min
select min(amount) as minimum 
from transactions;

-- avg
select avg(amount) as average 
from transactions;

-- sum
select sum(amount) as maximum 
from transactions;

select * from employees;

-- concat 
select concat(first_name, " ",last_name) as full_name
from employees;

-- LOGICAL OPERATORS 
alter table employees 
add column job varchar(25) after hourly_pay;
select * from employees;

update employees
set job = "janitor"
where employee_id =6;
select * from employees;

-- 	AND 
-- both statements need to be true 
select * from employees
where hire_date < "2026-02-16" and job = "cook";


-- OR 
-- only one condition needs to be true
select * from employees
where job = "cook" or job = "cashier";

-- NOT Reverses anything u put down 
select * from employees
where not job = "cook";

-- combining logical opperators 
select * from employees
where not job = "manager" and not job = "assistent manager";

-- BETWEEN working with the same column ]
select * from employees
where hire_date between "2026-02-13" and "2026-02-15";

-- IN 
select * from employees
where job in ("cook", "cashier", "janitor");

commit;


-- WILD CARD CHARACTER 
-- USED TO SUBSTITUTE ONE OR MORE CHARACTERS IN A STRING 
-- % - represents any amount of random characters 
-- _ - represents any random letter
select * from employees
where first_name like "s%";

select * from employees
where job like "_ook";


select * from employees
where hire_date like "____-02-__";

-- Order By 
-- Sorts a column either asc or dsc 
-- asc by default 
select * from employees
order by first_name  asc;

select * from transactions
order by amount, customer_id asc;

-- LIMIT clause is used to limit the number of records 
-- useful if you are working with a lot of data 
-- can be used to display a large data on pages like pagination 

select * from customers
order by last_name limit 4;

-- offset 
-- the first number controlls the offset of the limit, limits the number of rows quried 
select * from customers
order by last_name limit 2, 2;


-- Union opperators 
-- combines the results of 2 or more select statements 
-- they need to have the same amount of columns for it to work
-- select a spesific amount of columns 
-- union, union all (doesnt allow duplicates)
select first_name, last_name from employees 
union
select first_name, last_name from customers
order by first_name asc;

-- self joins 
-- join another copy of a table to itself 
-- used to compare rows of the same table 
-- helps to display a heirachy of data

alter table customers
add referral_id int;

update customers 
set referral_id = 2
where customer_id = 4;

select a.customer_id, a.first_name, a.last_name, Concat(b.first_name, " ",b.last_name) as referred_by
from customers as a
inner join customers as b
on a.referral_id = b.customer_id;

set sql_safe_updates =0;
alter table employees add supervisor_id int;
update employees
set supervisor_id = 3
where employee_id = 6;
select * from employees;

alter table employees 
drop column superviosor_id;

select a.first_name, a.last_name, concat(b.first_name," ", b.last_name ) as "reports_to"
from employees as a
inner join employees as b
on a.supervisor_id = b.employee_id;

commit;
-- views 
-- virtual tables based on the result of a sql statement, 
-- the fields in a view are from one or more real tables in the database 
-- they are not real tables but can be interacted with as if they were 
-- updates automatically 

select * from employees;

create view employee_attendence as 
select first_name, last_name 
from employees;

select * from employee_attendence;

-- drop a view 
drop view employee_attendence;

select * from customers;

alter table customers 
add column email varchar(50);

update customers 
set email = "Ppuff@gmail.com"
where customer_id =4;

create view customer_emails as select email from customers;

select * from customer_emails;

insert into customers 
values (5,"Pearl","Kraks", Null,"PKrabs@gmail.com");

-- INDEXES ]
-- used to find values within a specific column more quickly 
-- MYSQL searches squentailly through a coulmn so the longer the column the more expensive the operation is
-- UPDATE will take longer than a SELECT 

select * from customers;

-- searching for indexes 
-- we can locate a customer by using the primary key not so much there name or last name 
show indexes from customers;

-- create index 
create index last_name_idx
on customers(last_name);


-- now we can search for a customer using there last name 
select * from customers 
where last_name = "Puff";

create index first_name_idx
on customers(first_name);

-- creating multi index 
create index last_name_first_name_idx
on customers(last_name, first_name);

show indexes from customers;

alter table customers 
drop index first_name_idx;

select * from customers 
where last_name = "Puff";

