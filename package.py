class Package:
    """Data model for one package plus mutable delivery lifecycle fields."""

    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, notes):
        # Static package metadata loaded from CSV.
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes

        # Mutable simulation state updated as trucks are dispatched and deliveries occur.
        self.status = "At hub"
        self.delivery_time = None
        self.truck_id = None

    def __str__(self):
        """Return full package details for debugging and audit-style output."""
        return (
            f"Package ID: {self.package_id}, Address: {self.address}, City: {self.city}, "
            f"State: {self.state}, Zip: {self.zip_code}, Deadline: {self.deadline}, "
            f"Weight: {self.weight}kg, Notes: {self.notes}, Status: {self.status}, "
            f"Delivery Time: {self.delivery_time}, Truck ID: {self.truck_id}"
        )