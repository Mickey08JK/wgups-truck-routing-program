from datetime import timedelta

class Truck:
    """
    Represents a delivery truck for the routing program.
    Mutable state container for one truck's route simulation.
    Tracks packages, location, mileage, and timeline progression.
    """
    def __init__(self, truck_id, departure_time, packages):
        self.truck_id = truck_id
        self.packages = packages                        # Remaining package IDs for this truck.
        self.current_location = "4001 South 700 East"   # Starts at the hub.
        self.departure_time = departure_time            # Scheduled route start timestamp.
        self.current_time = departure_time              # Advances as each segment is traveled.
        self.mileage = 0.0                              # Cumulative miles traveled.
        self.hub_address = "4001 South 700 East"        # Hub reference address.