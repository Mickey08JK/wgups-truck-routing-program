# WGUPS Truck Routing Program

This project simulates package delivery for WGUPS using a nearest-neighbor routing approach, package constraints, and time-based status tracking.

## Program Flow

1. Load package records into a hash table keyed by package ID.
2. Apply known constraints (delayed packages and incorrect-address timeline).
3. Load address and distance data into a lookup-friendly matrix.
4. Dispatch Truck 1 and Truck 2 at fixed departure times.
5. Dispatch Truck 3 after Truck 1 returns.
6. Update package 9 address before Truck 3 route execution.
7. Run CLI to query package status at any historical time and view total mileage.

## Routing Strategy

- Delivery uses a greedy nearest-neighbor loop per truck.
- At each stop, the truck selects the closest remaining package destination.
- Travel time is computed with a fixed speed assumption of 18 mph.

## Time Simulation Rules

- Package states transition through: At Hub/Delayed -> En Route -> Delivered.
- Delayed packages (6, 25, 28, 32) are unavailable until 9:05 AM.
- Package 9 remains delayed until its address is corrected at 10:20 AM.

## Data Inputs

- packages.csv: package metadata and special notes.
- distances.csv: address list plus distances (triangular/partial matrix normalized in code).

## File Responsibilities

- main.py: orchestrates setup, truck dispatch timeline, and UI launch.
- deliver_packages.py: nearest-neighbor route execution and delivery timestamp updates.
- ui.py: interactive status queries by package or full snapshot at user-selected time.
- load_package_data.py: package CSV parsing and hash table population.
- load_distance_data.py: distance CSV parsing and matrix normalization.
- hash_table.py: separate-chaining hash table implementation.
- package.py: package domain model with mutable lifecycle fields.
- truck.py: truck state model (location, time, mileage, assigned package IDs).
