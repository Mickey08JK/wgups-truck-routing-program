import csv


def load_distance_data(filename):
    """
    Read address and distance data from CSV.

    Expected CSV shape per row:
    - column 0: canonical address string
    - remaining columns: distances to other addresses

    The source table may be triangular/partial. This loader normalizes it into
    a full symmetric matrix so lookups can be done directly by index.

    Returns:
        address_list: list of address strings (index = address_id)
        distance_matrix: 2d list of floats (symmetric)
    """
    address_list = []
    distance_matrix = []
    with open(filename, encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        for row in reader:
            # Row address labels are used by routing and package address matching.
            address_list.append(row[0].strip())
            distances = [float(x) if x else 0.0 for x in row[1:]]
            distance_matrix.append(distances)

    # Normalize to a square symmetric matrix for direct [i][j] access.
    num_addresses = len(address_list)
    for i in range(num_addresses):
        while len(distance_matrix[i]) < num_addresses:
            distance_matrix[i].append(0.0)  # Pad with zeros if necessary
        for j in range(num_addresses):
            if distance_matrix[i][j] == 0.0 and i != j:
                distance_matrix[i][j] = distance_matrix[j][i]
    
    return address_list, distance_matrix




def get_distance(address1, address2, address_list, distance_matrix):
    """Return miles between two addresses using matrix lookup by address index."""
    index1 = address_list.index(address1)
    index2 = address_list.index(address2)
    return distance_matrix[index1][index2]