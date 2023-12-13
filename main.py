from csv import reader
import json
import pandas as pd
from prettytable import from_csv
from collections import namedtuple
import pandasql as sql


# class phonebook:
#     def __init__(self,file_path):
#         self.file_path = file_path
#         self.phonebook = self.load_data()


def read_phonebook_from_csv_or_json(file_path: str):
    
    """
    Read the phonebook data from a CSV file.
    
    Args:
        path (str): The path to the CSV file.
    
    Returns:
        list: A list containing the rows of the CSV file.
    """
    phone_records = []
    if file_path.endswith(".csv"):
        with open(file_path,'r') as f:
            csv_reader = reader(f)
            next(csv_reader)
            for row in csv_reader:
                 phone_records.append(
                 {
                    "Name": row[0],
                    "email": row[1],
                    "Phone 1": row[2],
                    "Phone 2": row[3]
                    })
            df = pd.DataFrame(phone_records)
            return df
    elif file_path.endswith(".json"):
        with open(file_path,'r') as f:
            json_reader = json.load(f)
            for row in json_reader:
                phone_records.append({
                    "Name": row["name"],
                    "email": row["email"],
                    "Phone 1": row["phone1"],
                    "Phone 2": row["phone2"]
                    })
            df = pd.DataFrame.from_dict(phone_records)
            return df
    else: 
        raise Exception(f"Unsupported file format:{file_path}")
    



phone_records = read_phonebook_from_csv_or_json("phonebook.csv")
print(type(phone_records))
print(phone_records)
