# Hospital Patient Management System

## Project Description

The **Hospital Patient Management System** is a simple Python-based
project designed to manage basic patient records in a hospital. It
allows users to add, view, search, and delete patient information
through a menu-driven interface.

Patient details such as Patient ID, Name, Age, Gender, Disease, Doctor,
and Room Number are stored in a CSV file. The project demonstrates
fundamental Python concepts including functions, loops, conditional
statements, CSV file handling, lists, and dictionaries.

## Features

-   Add a new patient
-   Display all patient records
-   Search for a patient using Patient ID
-   Delete a patient record
-   Store patient data permanently in `patients.csv`
-   Simple command-line menu

## Technologies Used

-   Python 3
-   CSV file handling
-   `csv` module
-   `os` module

## Project Structure

``` text
Hospital-Patient-Management/
│
├── hospital_management.py
├── patients.csv
└── README.md
```

## How to Run

1.  Install Python 3 on your computer.
2.  Save the Python program as `hospital_management.py`.
3.  Open a terminal in the project folder.
4.  Run:

``` bash
python hospital_management.py
```

5.  Select an option from the menu.

## Menu Options

``` text
1. Add Patient
2. Show Patients
3. Search Patient
4. Delete Patient
5. Exit
```

## Data Storage

The program automatically creates a `patients.csv` file if it does not
already exist. The CSV file stores:

-   Patient ID
-   Name
-   Age
-   Gender
-   Disease
-   Doctor
-   Room

## Python Concepts Demonstrated

-   Functions
-   Variables
-   `if-elif-else` statements
-   `while` loops
-   `for` loops
-   Lists
-   Dictionaries
-   CSV file handling
-   File operations
-   User input

## Objective

The main objective of this project is to demonstrate how basic Python
programming and file handling can be used to create a simple real-world
hospital record management application.

## Future Improvements

The project can be extended by adding:

-   Patient update functionality
-   Appointment management
-   Billing system
-   Doctor management
-   Login authentication
-   Graphical user interface
-   Database connectivity using SQLite or MySQL

## Disclaimer

This is an educational first-year engineering project and is not
intended for use as a production hospital information system.
