#Randal McKee 011094452

from load_package_data import load_package_data
from load_distance_data import load_distance_data
from hash_table import ChainingHashTable
from package import Package

def main():
    # Create a hash table to store packages
    package_hash_table = ChainingHashTable()

    # Load package data from CSV file into the hash table
    load_package_data('packages.csv', package_hash_table)

    # **REMOVE** TEST: Retrieve and print a package by ID
    pkg_id_to_find = 9  # Change this to test with different package IDs
    package = package_hash_table.search(pkg_id_to_find)
    if package:
        print(f"Package ID: {package.package_id}")
        print(f"Address: {package.address}")
        print(f"City: {package.city}")
        print(f"State: {package.state}")
        print(f"Zip Code: {package.zip_code}")
        print(f"Delivery Deadline: {package.deadline}")
        print(f"Weight: {package.weight}")
        print(f"Special Notes: {package.notes}")
    else:
        print(f"Package with ID {pkg_id_to_find} not found.")
    
    
    # In main.py — temporary test
    address_list, distance_matrix = load_distance_data("distances.csv")

    print(f"Loaded {len(address_list)} addresses")  # Should be 27
    print(f"First address: '{address_list[0]}'")     # Should be "4001 South 700 East"
    print(f"HUB to 1060 Dalton: {distance_matrix[0][1]}")  # Should be 7.2
    print(f"1060 Dalton to HUB: {distance_matrix[1][0]}")  # Should be 7.2 (mirrored)

    # Print all addresses to visually verify
    for i, addr in enumerate(address_list):
        print(f"  [{i}] {addr}")


if __name__ == "__main__":
    main()