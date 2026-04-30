class Truck:
    """
    Represents a delivery truck for the routing program.
    Tracks packages, locationk, mileage, and time during delivery.
    """
    def __init__(self, truck_id, departure_time, packages):
        self.truck_id = truck_id
        self.packages = packages                        # List of package IDs to deliver
        self.current_location = "4001 South 700 East"   # Starting location is HUB
        self.departure_time = departure_time            # datetime object
        self.current_time = departure_time              # Tracks time during delivery
        self.mileage = 0.0                              # Total mileage driven
        self.hub_address = "4001 South 700 East"        # HUB address for reference