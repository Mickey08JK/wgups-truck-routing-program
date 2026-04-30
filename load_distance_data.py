import csv


def load_distance_data(filename):
    """
    Reads distance data from csv file.
    Returns:
        address_list: list of address strings (index = address_id)
        distance_matrix: 2d list of floats (symmetric)
    """
    address_list = []
    distance_matrix = []
    with open(filename, encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        for row in reader:
            address_list.append(row[0].strip())
            distances = [float(x) if x else 0.0 for x in row[1:]]
            distance_matrix.append(distances)

    # Ensure the distance matrix is symmetric
    num_addresses = len(address_list)
    for i in range(num_addresses):
        while len(distance_matrix[i]) < num_addresses:
            distance_matrix[i].append(0.0)  # Pad with zeros if necessary
        for j in range(num_addresses):
            if distance_matrix[i][j] == 0.0 and i != j:
                distance_matrix[i][j] = distance_matrix[j][i]
    
    return address_list, distance_matrix




def get_distance(address1, address2, address_list, distance_matrix):
    '''
    Returns the distance in miles between two addresses
    '''
    index1 = address_list.index(address1)
    index2 = address_list.index(address2)
    return distance_matrix[index1][index2]