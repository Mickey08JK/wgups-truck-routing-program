import csv
from hash_table import ChainingHashTable
from package import Package

def load_package_data(filename, hash_table):
    """
    Reads package data from a CSV and inserts each package 
    into the provided hash table using package ID as the key.
    """
    with open(filename, encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            pkg_id = int(row[0])
            address = row[1].strip()
            city = row[2].strip()
            state = row[3].strip()
            zip_code = row[4].strip()
            delivery_deadline = row[5].strip()
            weight = row[6].strip()
            special_notes = row[7].strip() if len(row) > 7 else ""

            package = Package(pkg_id, address, city, state, zip_code, delivery_deadline, weight, special_notes)
            hash_table.insert(pkg_id, package)