# RentSpaces-App

To Run The application download the python scripts and install mysqlconnector(Run command pip3 install mysql-connector-python) and tkcalender(pip3 install tkcalender)
If you have mysql you can run the sql file and get the database inside your system too. Change the host-name, password, user, database-name in the scripts file.

Our Car Rental Company “RentSpaces” keeps a number of offices in many cities. Each office maintains a number of cars with many carTypes.
The Car types include: Mini,Truck,Van,Prime,Sedan.

“RentSpaces” maintains a list of all their customers. When a customer first signs in to the portal, customer name, email_ID, address and phone number is recorded. A customer is identified by a unique customer id generated on signing up in the portal.

A customer can (transactions possible) rent a vehicle(followed by advanced payment based on number of days of rent), reserve this vehicle for specific days , return the vehicle that he/she has rented.

To make a reservation, a customer provides the city, the type of vehicle, the day and time for which he/she would like to pick up and return the vehicle.
When a customer returns the vehicle, we record the date,  the time, and the gauge reading whether the car tank is full.
After this the availability of the car is provided back in the database, and the user makes the remaining payment to the company.

If some car is already booked a user can add a request for the car which will add him to a waiting list in which later based on the availability we will message him the availability of the car. The no of requests for the car is then updated.
