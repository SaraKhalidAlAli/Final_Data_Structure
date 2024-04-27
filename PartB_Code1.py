import heapq

# Class for representing the road connections between nodes in the graph.
class Road:
    def __init__(self, pathway_id, distance):
        self.pathway_id = pathway_id
        self.distance = distance

  # Class for the network graph which contains the nodes and their respective edges.
class NetworkGraph:
    def __init__(self):
        # Dictionary to store the nodes and their corresponding edges
        self.nodes = {}

    # Method to add a new node to the graph
    def add_node(self, point):
        if point not in self.nodes:
            self.nodes[point] = {}
      
    # Method to connect two nodes with an edge (road)
    def connect_nodes(self, origin, destination, pathway_id, distance):
        if origin not in self.nodes:
            self.add_node(origin)
        if destination not in self.nodes:
            self.add_node(destination)
        self.nodes[origin][destination] = Road(pathway_id, distance)
        self.nodes[destination][origin] = Road(pathway_id, distance)

# Function for the search algorithm used to find the best path
def best_first_search(network, start_point):
    # Priority queue to hold nodes to visit with cost, current node, and path taken
    queue = [(0, start_point, [])]
    # Set to keep track of nodes where deliveries have been completed
    completed_deliveries = set()
    # Dictionary to store the delivery paths to each house and the cost
    delivery_routes = {}

    # Loop through the queue until it's empty or all deliveries are made
    while queue:
        distance_travelled, current_point, route = heapq.heappop(queue)
        if current_point.startswith('H') and current_point not in completed_deliveries:
            completed_deliveries.add(current_point)
            delivery_routes[current_point] = (route + [current_point], distance_travelled)
        if len(completed_deliveries) == len([node for node in network.nodes if node.startswith('H')]):
            break
        for adjacent, road in network.nodes[current_point].items():
            if adjacent not in completed_deliveries or not adjacent.startswith('H'):
                heapq.heappush(queue, (distance_travelled + road.distance, adjacent, route + [current_point]))

    return delivery_routes

# Function to execute predefined test scenarios
def run_test_cases(network):
    # Predefined start points for test cases
    test_starts = ['1', '6', '12']
    for test_start in test_starts:
        print(f"Initiating delivery from junction: {test_start}")
        delivery_routes = best_first_search(network, test_start)
        for destination, (route, distance_travelled) in delivery_routes.items():
            print(f"Delivered to {destination}: Route taken: {' -> '.join(route)}, Total distance: {distance_travelled}")
        print("\n" + "="*50 + "\n")

  # Entry point of the script
def main():
    # Instantiate the network graph
    network = NetworkGraph()

    # Data to populate the graph with nodes and their connections
    data = {
        '1': {'2': 60, '5': 45},
        '2': {'1': 60, 'H1': 4, '6': 16, '3': 30},
        '3': {'2': 30, '7': 44, '4': 30},
        '4': {'3': 30, '8': 45},
        '5': {'1': 45, '6': 77, '9': 13},
        '6': {'5': 77, 'H2': 6, '2': 16, '7': 9, '10': 12},
        '7': {'6': 9, '3': 44, '8': 5, '11': 14},
        '8': {'4': 45, 'H3': 10, '7': 5, '12': 11},
        '9': {'5': 13, 'H4': 7, '10': 65},
        '10': {'H4': 7, '9': 65, '6': 12, '11': 16},
        '11': {'10': 16, '7': 14, '12': 11},
        '12': {'11': 33, 'H5': 10, '8': 11}
    }

    # Populate the network graph with data
    for origin, connections in data.items():
        for destination, road_length in connections.items():
            pathway_id = f"{origin}-{destination}"
            network.connect_nodes(origin, destination, pathway_id, road_length)

    # Execute the test scenarios
    run_test_cases(network)

# Ensure that the script runs only when executed directly
if __name__ == "__main__":
    main()
