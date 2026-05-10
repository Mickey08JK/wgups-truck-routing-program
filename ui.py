from datetime import datetime


def get_status_at_time(package, check_time, truck_departure_times):
    '''Returns the status of a package at a given time, considering truck departure times.'''
    truck_depart = truck_departure_times.get(package.truck_id)

    # If truck hasn't left yet, package is at hub or delayed
    if truck_depart is None or check_time < truck_depart:
        #check if delayed
        if package.package_id in [6, 25, 28, 32]:
            if check_time < datetime(2026, 1, 1, 9, 5, 0):
                return "Delayed"
        if package.package_id == 9:
            if check_time < datetime(2026, 1, 1, 10, 20, 0):
                return "Delayed"
        return "At Hub"
    
    # If package has been delivered and check time is after delivery
    if package.delivery_time and check_time >= package.delivery_time:
        return f"Delivered at {package.delivery_time.strftime('%I:%M %p')}"
    
    # Else it's on truck en route
    return "En Route"

def user_interface(package_hash_table, truck1, truck2, truck3):
    '''Provides command line interface to check package status at any time and view mileage.'''

    # Store departure times for lookup
    truck_departure_times = {
        1: truck1.departure_time,
        2: truck2.departure_time,
        3: truck3.departure_time
    }

    total_mileage = truck1.mileage + truck2.mileage + truck3.mileage

    # Create user menu and actions
    print("\n" + "=" * 60)
    print("  WGUPS Routing Program")
    print("=" * 60)
    print(f"  Total mileage: {total_mileage:.2f} miles")
    print("=" * 60)

    while True:
        print("\nOptions:")
        print("  1. Look up a single package at a specific time")
        print("  2. View all packages at a specific time")
        print("  3. Exit")

        choice = input("\nEnter choice (1-3): ").strip()

        if choice == '1':
            try:
                package_id = int(input("Enter package ID (1-40): ").strip())
                time_str = input("Enter time (HH:MM in 24-hour format): ").strip()
                hours, minutes = map(int, time_str.split(":"))
                check_time = datetime(2026, 1, 1, hours, minutes, 0)

                package = package_hash_table.search(package_id)
                if package:
                    status = get_status_at_time(package, check_time, truck_departure_times)
                    print(f"\n  Package {package.package_id} at {check_time.strftime('%I:%M %p')}:")
                    print(f"  Address:  {package.address}, {package.city}, {package.state} {package.zip_code}")
                    print(f"  Deadline: {package.deadline}")
                    print(f"  Weight:   {package.weight} kg")
                    print(f"  Truck:    {package.truck_id}")
                    print(f"  Status:   {status}")
                else:
                    print(f"  Package {package_id} not found.")
            except ValueError:
                print("  Invalid input. Please enter a valid package ID and time (HH:MM in 24-hour format e.g. 09:30).")

        elif choice == '2':
            try:
                time_str = input("Enter time (HH:MM in 24-hour format): ").strip()
                hours, minutes = map(int, time_str.split(":"))
                check_time = datetime(2026, 1, 1, hours, minutes, 0)

                print(f"\n  All packages at {check_time.strftime('%I:%M %p')}:")
                print(f"  {'ID':<5} {'Address':<40} {'Deadline':<12} {'Truck':<7} {'Status'}")
                print("  " + "-" * 90)

                for package_id in range(1, 41):
                    package = package_hash_table.search(package_id)
                    status = get_status_at_time(package, check_time, truck_departure_times)
                    print(f"  {package.package_id:<5} {package.address:<40} {package.deadline:<12} {package.truck_id:<7} {status}")
            except ValueError:
                print("  Invalid input. Please enter a valid time (HH:MM in 24-hour format e.g. 09:30).")

        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("  Invalid choice. Please enter 1, 2, or 3.")