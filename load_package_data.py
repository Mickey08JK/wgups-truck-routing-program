import csv
from hash_table import ChainingHashTable
from package import Package

def load_package_data(filename, hash_table):
    """
    Read package rows from CSV and insert Package objects into hash table.

    CSV schema order:
    id, address, city, state, zip, deadline, weight, optional notes

    Package ID is used as the key to support efficient routing/UI lookups.
    """
    with open(filename, encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header because row parsing below assumes data columns.
        for row in reader:
            pkg_id = int(row[0])
            address = row[1].strip()
            city = row[2].strip()
            state = row[3].strip()
            zip_code = row[4].strip()
            delivery_deadline = row[5].strip()
            weight = row[6].strip()
            special_notes = row[7].strip() if len(row) > 7 else ""

            # Create domain object and store it for later simulation steps.
            package = Package(pkg_id, address, city, state, zip_code, delivery_deadline, weight, special_notes)
            hash_table.insert(pkg_id, package)