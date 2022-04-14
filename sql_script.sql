drop table if exists listings;
drop table if exists reservation;
drop table if exists car;
drop table if exists carType;
drop table if exists customer;
drop table if exists office;

create table office
(
office_ID INT UNSIGNED auto_increment,
office_city varchar(20) not null,
primary key( office_ID)
);

create table customer
(
customerid int unsigned auto_increment,
name varchar(20) not null,
phoneno decimal(10,0) not null,
email varchar(30) not null,
password varchar(20) not null,
status bool default 0,
balance int not null default 10000,
messages varchar(75) not null default 'Book Your Own Space!',

primary key(customerid)
);

create table carType
( 
type_ID int unsigned auto_increment,
office_ID int unsigned  not null,
car_type varchar(20) not null,
price_per_day int not null,
tank_Capacity int not null default 20,

primary key(type_ID),
foreign key(office_ID) references office(office_ID) on delete cascade
);

create table car
(
car_ID  int unsigned auto_increment,
type_ID  int unsigned ,
car_name varchar(20) not null,
status boolean default 0,
requests int default 0,
primary key(car_ID),
foreign key(type_ID) references carType(type_ID)
);
create table reservation
(
reservation_ID INT UNSIGNED auto_increment,
customerid INT UNSIGNED,
    car_ID INT UNSIGNED,
    issue_date date,
    req_days INT UNSIGNED,
	primary key (reservation_ID),
  foreign key (customerid) REFERENCES customer(customerid) ON DELETE CASCADE,
  foreign key (car_ID) REFERENCES car(car_ID) ON DELETE CASCADE
);

create table listings
(
request_ID int unsigned auto_increment ,
car_ID int unsigned not null,
customer_ID int unsigned not null,
date_time TIMESTAMP default CURRENT_TIMESTAMP,
primary key(request_ID),
foreign key(car_ID) references car(car_ID),
foreign key(customer_ID) references customer(customerid)
);

insert into customer  (name,phoneno,email,password) values
("Shashank",9876543210,"abc@gmail.com","12345"),
("Akhil",	9999999999	,"efg@gmail.com"	,"12345"),
("gud_guy",	9879879879	,"Enter Your Email"	,"Enter Your Password"),
("Shadan",	9876587654	,"asd@gmail.com"	,"2345"),
("ramesh" , 6754839201, "adsjf@gmail.com", "qwerty"),
("suresh", 9102836345, "zxcv@gmail.com", "asdfg");

insert into office(office_city) values
("Jaipur"), ("Delhi"), ("Pilani"), ("Goa"), ("Hyderabad"), ("Mumbai"), ("Kolkata");

insert into carType(type_ID, office_ID, car_type,price_per_day) values


(185, 1, "Mini", 1200),
(186, 1, "Truck", 1250),
(187, 1, "Van", 1300),
(188, 1, "Prime", 1350),
(189, 1, "Sedan", 1400),
(190, 1, "Sports", 1450),
(191, 2, "Mini", 1500),
(192, 2, "Truck", 1550),
(193, 2, "Van", 1600),
(194, 2, "Prime", 1650),
(195, 2, "Sedan", 1700),
(196, 2, "Sports", 1750),
(197, 3, "Mini", 1800),
(198, 3, "Truck", 1850),
(199, 3, "Van", 1900),
(200, 3, "Prime", 1950),
(201, 3, "Sedan", 2000),
(202, 3, "Sports", 2050),
(203, 4, "Mini", 2100),
(204, 4, "Truck", 2150),
(205, 4, "Van", 2200),
(206, 4, "Prime", 2250),
(207, 4, "Sedan", 2300),
(208, 4, "Sports", 2350),
(209, 5, "Mini", 2400),
(210, 5, "Truck", 2450),
(211, 5, "Van", 2500),
(212, 5, "Prime", 2550),
(213, 5, "Sedan", 2600),
(214, 5, "Sports", 2650),
(215, 6, "Mini", 2700),
(216, 6, "Truck", 2750),
(217, 6, "Van", 2800),
(218, 6, "Prime", 2850),
(219, 6, "Sedan", 2900),
(220, 6, "Sports", 2950),
(221, 7, "Mini", 3000),
(222, 7, "Truck", 3050),
(223, 7, "Van", 3100),
(224, 7, "Prime", 3150),
(225, 7, "Sedan", 3200),
(226, 7, "Sports", 3250);

insert into car(type_id, car_name) values
(185, "alto"),
(185, "maruti"),
(185, "wagonR"),
(185, "nano"),
(186,"Yamaha"),
(186,	"XYZ"),
(187,	"vc"),
(188,	"qwer"),
(189,	"titan"),
(190,	"SAVAN"),
(191,	"gop"),
(191,	"innova"),
(191,	"ferrari"),
(191,	"dugati"),
(201,	"baleno"),
(213,	"ertiga");

insert into reservation values
(1,1,4,'2022-04-10',3);
update car
set status = 1 where car_ID = 4;
update customer
set status = 1 where customerid = 1;

insert into listings (request_id,car_id,customer_id)
values
(1,4,2);
update car
set requests = 1 where car_id = 4;
 

