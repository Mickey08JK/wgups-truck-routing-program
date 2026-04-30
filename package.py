class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = "At hub"
        self.delivery_time = None
        self.truck_id = None

    def __str__(self):        return f"Package ID: {self.package_id}, Address: {self.address}, City: {self.city}, State: {self.state}, Zip: {self.zip_code}, Deadline: {self.deadline}, Weight: {self.weight}kg, Notes: {self.notes}, Status: {self.status}, Delivery Time: {self.delivery_time}, Truck ID: {self.truck_id}"