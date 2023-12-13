# VEngage_Assignment

Phonebook Application
This application allows you to manage a simple phonebook using SQL-like commands.

Features:

Load data from CSV or JSON files.
Read all records or specific records based on criteria.
Insert new records.
Delete records based on name.
Usage:

Install the required dependencies:
pip install csv json prettytable
Create a phonebook file (e.g., phonebook.csv or phonebook.json).

Run the application:

python phonebook.py
Use the following commands to interact with the phonebook:
SELECT * FROM phone_records;: Retrieves all records.
SELECT * FROM phone_records WHERE name='<name>';: Retrieves records where the name matches the provided value.
INSERT INTO phone_records(name, email, phone1, phone2) VALUES(<values>);: Inserts a new record with the specified values.
DELETE FROM phone_records WHERE name='<name>';: Deletes the record with the matching name.
Example:

$ phonebook.py

> SELECT * FROM phone_records;

+-------+---------+-------+-------+
| name  | email   | phone1 | phone2 |
+-------+---------+-------+-------+
| John  | john@example.com | 123456 | 654321 |
| Jane  | jane@example.com | 234567 | 765432 |
| Doe   | doe@example.com | 345678 | 876543 |
+-------+---------+-------+-------+

> SELECT * FROM phone_records WHERE name='doe';

+------+-------------+------------+------------+
| name |    email    |   phone1   |   phone2   |
+------+-------------+------------+------------+
| doe  | doe@abc.com | 9517534560 | 9638521470 |
+------+-------------+------------+------------+
Additional Notes:

The data is saved in the same format as the input file (CSV or JSON).
The application supports basic error handling and validation.

Contributing:

Feel free to contribute to this project by creating pull requests with improvements or bug fixes.
