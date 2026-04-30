import hash_table
from load_distance_data import load_distance_data, get_distance
import truck
from datetime import timedelta

def deliver_packages(truck, hash_table, get_distance, address_list, distance_matrix):
    """
    Uses the Nearest Neighbor algorithm to deliver all packages on a truck.
    For each stop, selects the closest undelivered package from the truck's
    current location, drives there, and delivers it.
    """
    while truck.packages:
        nearest_distance = float('inf')
        nearest_package = None

        # Find the nearest undelivered package
        for package_id in truck.packages:
            package = hash_table.search(package_id)
            distance = get_distance(truck.current_location, package.address, address_list, distance_matrix)

            if distance < nearest_distance:
                nearest_distance = distance
                nearest_package = package

        # Drive to the nearest package
        truck.mileage += nearest_distance
        truck.current_time += timedelta(hours=nearest_distance / 18)
        truck.current_location = nearest_package.address

        # Deliver the package
        nearest_package.status = "Delivered"
        nearest_package.delivery_time = truck.current_time

        # Remove the package from the truck's package list
        truck.packages.remove(nearest_package.package_id)