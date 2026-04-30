#Randal McKee 011094452

from deliver_packages import deliver_packages
from load_package_data import load_package_data
from load_distance_data import get_distance, load_distance_data
from hash_table import ChainingHashTable
from package import Package
from datetime import datetime
from truck import Truck


def main():
    # Create a hash table to store packages
    package_hash_table = ChainingHashTable()

    # Load package data from CSV file into the hash table
    load_package_data('packages.csv', package_hash_table)

    # Load distance data for algorithm use
    address_list, distance_matrix = load_distance_data("distances.csv")

    # Truck 1 - earliest deadlines and grouped packages
    truck1_packages = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
    truck1 = Truck(1, datetime(2026, 1, 1, 8, 0), truck1_packages)

    # Truck 2 - next set of deadlines and grouped packages
    truck2_packages = [3, 5, 6, 7, 8, 10, 18, 25, 27, 28, 32, 33, 35, 36, 38, 39]
    truck2 = Truck(2, datetime(2026, 1, 1, 9, 5, 0), truck2_packages)

    # Truck 3 - remaining packages
    truck3_packages = [2, 4, 9, 11, 12, 17, 21, 22, 23, 24, 26]
    truck3 = Truck(3, None, truck3_packages)


    """Run Truck 1 deliveries (departs at 8:00 AM)"""
    
    # Mark all packages on the truck as "En Route"
    for package_id in truck1.packages:
        package = package_hash_table.search(package_id)
        package.status = "En Route"
        package.truck_id = truck1.truck_id

    deliver_packages(truck1, package_hash_table, get_distance, address_list, distance_matrix)


    """Run Truck 2 deliveries (departs at 9:05 AM)"""

    # Mark all packages on the truck as "En Route"
    for package_id in truck2.packages:
        package = package_hash_table.search(package_id)
        package.status = "En Route"
        package.truck_id = truck2.truck_id

    deliver_packages(truck2, package_hash_table, get_distance, address_list, distance_matrix)

    # Truck 3 departs after Truck 1 returns to the hub
    truck3.departure_time = truck1.current_time
    truck3.current_time = truck1.current_time

    # Fix package 9's address and update its distance data before Truck 3 departs
    package_9 = package_hash_table.search(9)
    package_9.address = "410 S State St"
    package_9.zip_code = "84111"

    """Run Truck 3 deliveries"""
    
    # Mark all packages on the truck as "En Route"
    for package_id in truck3.packages:
        package = package_hash_table.search(package_id)
        package.status = "En Route"
        package.truck_id = truck3.truck_id

    deliver_packages(truck3, package_hash_table, get_distance, address_list, distance_matrix)

    # Total mileage calculation
    total_mileage = truck1.mileage + truck2.mileage + truck3.mileage
    print(f"Total mileage for all trucks: {total_mileage:.2f} miles")




if __name__ == "__main__":
    main()