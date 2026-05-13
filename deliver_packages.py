import hash_table
from load_distance_data import load_distance_data, get_distance
import truck
from datetime import timedelta

def deliver_packages(truck, hash_table, get_distance, address_list, distance_matrix):
    """
    Uses the Nearest Neighbor algorithm to deliver all packages on a truck.
    For each stop, selects the closest undelivered package from the truck's
    current location, drives there, and delivers it.

    This function mutates state in place:
    - truck mileage/time/location advance after each stop
    - package status changes to Delivered with a delivery timestamp
    - delivered package IDs are removed from truck.packages
    """
    # Continue routing until the truck's assigned package list is empty.
    while truck.packages:
        nearest_distance = float('inf')
        nearest_package = None

        # Evaluate all remaining packages and pick the nearest next stop.
        for package_id in truck.packages:
            package = hash_table.search(package_id)
            distance = get_distance(truck.current_location, package.address, address_list, distance_matrix)

            if distance < nearest_distance:
                nearest_distance = distance
                nearest_package = package

        # Travel model assumption: constant 18 mph across all route segments.
        truck.mileage += nearest_distance
        truck.current_time += timedelta(hours=nearest_distance / 18)
        truck.current_location = nearest_package.address

        # Mark delivery event at arrival time.
        nearest_package.status = "Delivered"
        nearest_package.delivery_time = truck.current_time

        # Remove delivered package so it is not reconsidered in the next iteration.
        truck.packages.remove(nearest_package.package_id)