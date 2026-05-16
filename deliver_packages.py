import hash_table
from load_distance_data import load_distance_data, get_distance
import truck
from datetime import timedelta, datetime

def deliver_packages(truck, hash_table, get_distance, address_list, distance_matrix):
    """
    Uses the Nearest Neighbor algorithm to deliver all packages on a truck.
    For each stop, selects the closest undelivered package from the truck's
    current location, drives there, and delivers it.

    This function mutates state in place:
    - truck mileage/time/location advance after each stop
    - package status changes to Delivered with a delivery timestamp
    - delivered package IDs are removed from truck.packages
    
    Special handling: Package 9 address is corrected at 10:20 AM during routing.
    Package 9 cannot be delivered until after its address is corrected.
    """
    # Continue routing until the truck's assigned package list is empty.
    while truck.packages:
        # Timeline event at 10:20 AM: package 9 receives corrected address during Truck 3 routing.
        if truck.truck_id == 3 and truck.current_time >= datetime(2026, 1, 1, 10, 20, 0):
            package_9 = hash_table.search(9)
            if package_9 and 9 in truck.packages and package_9.address != "410 S State St":
                package_9.address = "410 S State St"
                package_9.zip_code = "84111"
        
        nearest_distance = float('inf')
        nearest_package = None

        # Evaluate all remaining packages and pick the nearest next stop.
        # Skip package 9 until its address is corrected at 10:20 AM.
        for package_id in truck.packages:
            # Package 9 cannot be delivered until 10:20 AM correction
            if package_id == 9 and truck.current_time < datetime(2026, 1, 1, 10, 20, 0):
                continue
            
            package = hash_table.search(package_id)
            distance = get_distance(truck.current_location, package.address, address_list, distance_matrix)

            if distance < nearest_distance:
                nearest_distance = distance
                nearest_package = package

        # If no deliverable package found, advance time and try again
        if nearest_package is None:
            if 9 in truck.packages:
                # Still waiting for 10:20 AM to correct package 9
                next_correction_time = datetime(2026, 1, 1, 10, 20, 0)
                truck.current_time = next_correction_time
                continue
            else:
                break

        # Travel model assumption: constant 18 mph across all route segments.
        truck.mileage += nearest_distance
        truck.current_time += timedelta(hours=nearest_distance / 18)
        truck.current_location = nearest_package.address

        # Mark delivery event at arrival time.
        nearest_package.status = "Delivered"
        nearest_package.delivery_time = truck.current_time

        # Remove delivered package so it is not reconsidered in the next iteration.
        truck.packages.remove(nearest_package.package_id)