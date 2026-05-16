"""
Data Structures and Algorithms - C950
Task 2
Randal McKee 011094452

Program flow:
1) Load package and distance data.
2) Apply known package constraints (delays, corrected address timeline).
3) Dispatch trucks in timeline order and run nearest-neighbor delivery.
4) Launch UI for historical status lookups and mileage reporting.
"""

from deliver_packages import deliver_packages
from load_package_data import load_package_data
from load_distance_data import get_distance, load_distance_data
from hash_table import ChainingHashTable
from package import Package
from datetime import datetime
from truck import Truck
from ui import user_interface


def main():
    # Create central package storage for fast ID-based lookup during routing and UI queries.
    package_hash_table = ChainingHashTable()

    # Load all package records into memory.
    load_package_data('packages.csv', package_hash_table)

    # Constraint setup: these packages are not physically available at the hub until 9:05 AM.
    delayed_packages = [6, 25, 28, 32]
    for package_id in delayed_packages:
        package = package_hash_table.search(package_id)
        package.status = "Delayed"

    # Package 9 is also delayed because its address is invalid until 10:20 AM.
    package_9 = package_hash_table.search(9)
    package_9.status = "Delayed"

    # Load address labels and distance matrix used by the routing algorithm.
    address_list, distance_matrix = load_distance_data("distances.csv")

    # Truck 1: earliest deadlines and grouped packages, departs at 8:00 AM.
    truck1_packages = [1, 4, 13, 14, 15, 16, 19, 20, 21, 22, 29, 30, 31, 34, 37, 40]
    truck1 = Truck(1, datetime(2026, 1, 1, 8, 0), truck1_packages)

    # Truck 2: remaining early constraints, departs at 9:05 AM when delayed packages arrive.
    truck2_packages = [3, 5, 6, 7, 8, 10, 18, 25, 27, 28, 32, 33, 35, 36, 38, 39]
    truck2 = Truck(2, datetime(2026, 1, 1, 9, 5, 0), truck2_packages)

    # Truck 3: remaining packages, departure depends on Truck 1 return timeline.
    truck3_packages = [2, 9, 11, 12, 17, 23, 24, 26]
    truck3 = Truck(3, None, truck3_packages)


    """Dispatch Truck 1 deliveries (8:00 AM)."""
    
    # At departure, package state transitions from At Hub/Delayed to En Route.
    for package_id in truck1.packages:
        package = package_hash_table.search(package_id)
        package.status = "En Route"
        package.truck_id = truck1.truck_id

    deliver_packages(truck1, package_hash_table, get_distance, address_list, distance_matrix)


    """Dispatch Truck 2 deliveries (9:05 AM)."""

    # Mark package/truck assignment at departure for timeline-based status reporting.
    for package_id in truck2.packages:
        package = package_hash_table.search(package_id)
        package.status = "En Route"
        package.truck_id = truck2.truck_id

    deliver_packages(truck2, package_hash_table, get_distance, address_list, distance_matrix)

    # Truck 3 departs only after Truck 1 finishes (shared fleet/driver constraint model).
    truck3.departure_time = truck1.current_time
    truck3.current_time = truck1.current_time
    
    """Dispatch Truck 3 deliveries."""
    
    # Mark final truck's package status before route execution.
    for package_id in truck3.packages:
        package = package_hash_table.search(package_id)
        package.status = "En Route"
        package.truck_id = truck3.truck_id

    deliver_packages(truck3, package_hash_table, get_distance, address_list, distance_matrix)

    # Run interactive UI to query package statuses at arbitrary times and display total mileage.
    user_interface(package_hash_table, truck1, truck2, truck3)




if __name__ == "__main__":
    main()