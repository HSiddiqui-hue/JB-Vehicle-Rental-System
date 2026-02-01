JB Vehicle Rental System
Project Overview

The JB Vehicle Rental System is a console-based Python application developed as part of the MSE800 – Professional Software Engineering course.
The system automates the vehicle rental process by allowing customers to book vehicles and staff (administrators) to manage vehicles and rental reservations.

This project demonstrates the application of object-oriented programming (OOP) principles, role-based access control, and a service-layer architecture.

Features
Client (Customer)

User registration and login

View available vehicles

Book a vehicle by selecting rental dates

View personal reservations

View booking status and rental fee

Staff (Admin)

User registration and login

Add new vehicles

Update vehicle details

Delete vehicles

View all vehicles

View available vehicles

View all reservations

Approve or reject booking requests

View dashboard summary (innovative feature)

System Requirements

Python 3.10 or later

Visual Studio Code (recommended)

Anaconda (optional)

How to Run the Application

Download or clone the project folder.

Open the project in Visual Studio Code.

(Optional) Activate your Anaconda environment.

Ensure the folder structure is intact.

Run the application by executing the main program file:

python main.py

How to Use the System
Staff (Admin)

Register as a Staff user.

Login using your credentials.

Use the staff menu to:

Add, update, or delete vehicles

View all vehicles and reservations

Approve or reject booking requests

View the dashboard summary

Client (Customer)

Register as a Client user.

Login using your credentials.

Use the client menu to:

View available vehicles

Book a vehicle

View your reservations and booking status

Project Structure

JB Vehicle Rental System
├── blueprint
│ ├── user.py (User, Client, and Staff models)
│ ├── vehicle.py (Vehicle model)
│ └── reservation.py (Reservation model)
│
├── services
│ ├── user_ser.py (User registration and login logic)
│ ├── vehicle_ser.py (Vehicle management logic)
│ └── reservation_ser.py (Reservation and approval logic)
│
├── main.py (Main program and menu handling)
└── README.md (User documentation)

Design and Architecture

The system follows a service-layer architecture.

User interaction is handled through the console menus in main.py.

Business logic is separated into service modules.

Core entities such as users, vehicles, and reservations are defined using blueprint (model) classes.

Data is stored in memory using Python lists, acting as a simple database for this assignment.

Business Rules

A vehicle is considered available only if it does not have an approved reservation.

When a reservation is approved by staff, the associated vehicle becomes unavailable.

Rejected reservations do not affect vehicle availability.

Rental duration must be within the vehicle’s minimum and maximum allowed rental days.

Rental charges are calculated based on the rental duration.

Known Limitations

All data is stored in memory and is lost when the program terminates.

No persistent database is implemented.

No vehicle return or rental completion feature is included.

The system is console-based and does not include a graphical user interface.

License

This project is released under the MIT License and is intended for educational purposes.

Credits

Developer: Hassan Siddiqui
Course: MSE800 – Professional Software Engineering
Institution: Yoobee College of Creative Innovation

Version Control

The project is managed using Git and hosted on GitHub:
https://github.com/HSiddiqui-hue/JB-Vehicle-Rental-System