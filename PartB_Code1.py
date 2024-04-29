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

# Use breadth-first search to find the shortest route between two points.
def bfs_shortest_route(graph, start, finish):
    queue = [(start, [start])]  # Queue to manage the exploration, initialized with the starting point and its path
    visited = set()  # keepin track of the visited point
    delivery_routes = {} # Dictionary to store the delivery paths to each house and the cost


    # Loop through the queue until it's empty or all deliveries are made
    while queue:
        current_point, path = queue.pop(0)  #exploring/looking at the next point in the queue.
        if current_point == finish:
            return path  #if statnent for 'if' the destination is reached, return the path.
        if current_point not in visited:
            visited.add(current_point)
            for neighbor, _ in graph.nodes[current_point].items():
                if neighbor not in visited:
                    queue.append(
                        (neighbor, path + [neighbor]))  #here we r adding the neighboring points to the queue with updated path.

    return []  # If no route is found, return an empty path.

# Function to execute predefined test scenarios
def run_test_cases(graph):
    # Predefined start points for test cases
    test_starts = ['1', '6', '12']
    for test_start in test_starts:
        print(f"Initiating delivery from junction: {test_start}")
        delivery_routes = {}
        for house in graph.nodes.keys():
            if house.startswith('H'):
                route = bfs_shortest_route(graph, test_start, house)
                if route:
                    delivery_routes[house] = route
        for destination in delivery_routes:
            route = delivery_routes[destination]
            total_distance = sum(graph.nodes[route[i]][route[i + 1]].distance for i in range(len(route) - 1))
            print(f"Delivered to> {destination}: Route taken: {' >>> '.join(route)}, Tot distance: {total_distance}")
        print("\n" + "=" * 50 + "\n")

  # Entry point of the script
def main():
    # Instantiate the network graph
    graph = NetworkGraph()

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
            graph.connect_nodes(origin, destination, pathway_id, road_length)

    # Execute the test scenarios
    run_test_cases(graph)

# Ensure that the script runs only when executed directly
if __name__ == "__main__":
    main()
