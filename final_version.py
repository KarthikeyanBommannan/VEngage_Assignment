import csv
import json
from prettytable import PrettyTable

class Phonebook:
    def __init__(self: object, filename: str) -> None:
        self.filename = filename
        self.data = []
        self._load_data()

    def _load_data(self: object):
        """
        Load data from a file.

        Opens the specified file and loads its contents into the `data` attribute
        of the current instance. The file format is determined based on the
        file extension.

        Parameters:
            None

        Returns:
            None

        Raises:
            Exception: If the file format is not supported.
        """
        with open(self.filename) as file:
            if self.filename.endswith(".csv"):
                reader = csv.DictReader(file)
                self.data = [row for row in reader]
            elif self.filename.endswith(".json"):
                self.data = json.load(file)
            else:
                raise Exception(f"Unsupported file format: {file}")

    def read(self: object, query: str):
        """
        Performs a read operation on the phone_records database.

        Args:
            query (str): The query to execute on the database.

        Returns:
            list or dict: The result of the query. If the query is "SELECT * FROM phone_records;", returns a list of all records in the database. If the query is "SELECT * FROM phone_records WHERE <criteria>;", returns a filtered list of records based on the specified criteria. If the query is not supported, raises an Exception.

        Raises:
            Exception: If the query is not supported.

        """
        if query == "SELECT * FROM phone_records;":
            return self.data
        elif query.startswith("SELECT * FROM phone_records WHERE"):
            criteria = query.split("WHERE")[1].strip()
            key, value = criteria.split("=")
            key = key.strip().lower()
            value = value.strip().strip(";").strip("'")
            filtered_data = [record for record in self.data if record[key].lower() == value.lower()]
            return filtered_data
        else:
            raise Exception(f"Unsupported query: {query}")

    def insert(self: object, query: str):
        """
        Inserts a new record into the phone_records table.

        Parameters:
            query (str): The query string to be executed.

        Returns:
            None

        Raises:
            Exception: If the query is not supported.
        """
        if query.startswith("INSERT INTO phone_records"):
            self._load_data()
            values = query.split("VALUES(")[1].split(")")[0].strip().strip("'")
            values_list = [val.strip() for val in values.split(",")]
            new_record = {
                "name": values_list[0],
                "email": values_list[1],
                "phone1": values_list[2],
                "phone2": values_list[3],
            }
            self.data.append(new_record)
            self._save_data()
        else:
            raise Exception(f"Unsupported query: {query}")

    def delete(self: object, query: str):
        """
        Deletes a record from the phone_records based on the provided query.

        Parameters:
            query (str): The query used to identify the record to be deleted.

        Returns:
            None

        Raises:
            Exception: If no record is found with the provided name in the query.
        """
        if query.startswith("DELETE FROM phone_records WHERE name="):
            name = query.split("=")[1].strip().strip(";").strip("'")
            for i, record in enumerate(self.data):
                if record["name"].lower() == name.lower():
                    del self.data[i]
                    self._save_data()
                    return
            raise Exception(f"No record found with name '{name}'")

    def _save_data(self: object):
        """
        Saves the data to a file.

        This function saves the data stored in the `self.data` attribute to a file specified by `self.filename`.
        The data is saved in either CSV or JSON format depending on the file extension of `self.filename`.
        
        Parameters:
        - None

        Returns:
        - None
        """
        with open(self.filename, "w") as file:
            if self.filename.endswith(".csv"):
                fieldnames = ["name", "email", "phone1", "phone2"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.data)
            elif self.filename.endswith(".json"):
                json.dump(self.data, file, indent=4)

    def print_sql_like_output(self: object,data: list):
        """
        Print the SQL-like output in a formatted table.

        Parameters:
        - data (list of dictionaries): The data to be printed in a table format.

        Returns:
        - None

        This function takes in a list of dictionaries representing records and prints
        them in a formatted table. If the data is empty, it prints a message indicating
        no matching records were found.
        """
        if not data:
            print("No matching records found.")
            return None

        table = PrettyTable(data[0].keys())
        for record in data:
            table.add_row(record.values())
        print(table)
        


phone_records = Phonebook("phonebook.csv")

results = phone_records.read("SELECT * FROM phone_records;")
phone_records.print_sql_like_output(results)

results = phone_records.read("SELECT * FROM phone_records WHERE name='doe';")
phone_records.print_sql_like_output(results)

phone_records.insert("INSERT INTO phone_records(name, email, phone1, phone2) VALUES('Test', 'test@test.xyz', '1234456', '1233233')")

phone_records.delete("DELETE FROM phone_records WHERE name='john'")
