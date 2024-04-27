import heapq


# Represents a connection between two points in the graph.
class Connection:
    def __init__(self, route_id, distance):
        self.route_id = route_id
        self.distance = distance


# Represents the entire map of connections.
class MapGraph:
    def __init__(self):
        # Holds the points and their respective connections in the graph.
        self.points = {}

    # Adds a new point to the map.
    def insert_point(self, point):
        # Ensures the point is unique before adding.
        if point not in self.points:
            self.points[point] = {}

    # Establishes a bidirectional route between two points.
    def construct_route(self, start_point, end_point, route_id, distance):
        # Automatically adds points if they don't already exist in the graph.
        if start_point not in self.points:
            self.insert_point(start_point)
        if end_point not in self.points:
            self.insert_point(end_point)
        self.points[start_point][end_point] = Connection(route_id, distance)
        self.points[end_point][start_point] = Connection(route_id, distance)


# Uses Dijkstra's algorithm to find the shortest route between two points.
def dijkstra_shortest_route(graph, start, finish):
    queue = [(0, start, [])]  # Queue to manage the exploration, initialized with the starting point.
    distances = {point: float('infinity') for point in graph.points}  # Track the shortest distance to each point.
    distances[start] = 0  # Distance to the start point is zero.
    visited = set()  # Keeps track of visited points.

    while queue:
        # Explore the point with the shortest distance next.
        current_distance, current_point, route = heapq.heappop(queue)
        if current_point not in visited:
            visited.add(current_point)
            route = route + [current_point]
            # If the current point is the destination, return the route and distance.
            if current_point == finish:
                return route, current_distance
            for neighbor, connection in graph.points[current_point].items():
                if neighbor not in visited:
                    new_distance = current_distance + connection.distance
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        heapq.heappush(queue, (new_distance, neighbor, route))

    return [], float('infinity')  # If no route is found, return an empty route and infinite distance.


# Function to perform predefined test cases to validate the shortest route logic.
def run_test_cases(graph):
    test_pairs = [
        ('1', '12', "\nScenario 1: Find shortest route from Point 1 to Point 12"),
        ('6', 'H5', "\nScenario 2: Find shortest delivery route from Point 6 to House H5"),
        ('9', 'H2', "\nScenario 3: Find shortest delivery route from Point 9 to House H2")]

    for start, end, description in test_pairs:
        print(description)
        route, total_distance = dijkstra_shortest_route(graph, start, end)
        print(f"Identified shortest route: {' >>> '.join(route)}, Total distance covered: {total_distance} meters.\n")
        print("\n" + '-' * 100)


# Main function to instantiate the graph and populate it with data.
def main():
    map_graph = MapGraph()

    # Each key-value pair in the dictionary represents a point and its directly connected routes.
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

    # Adding routes based on the provided data to the map graph.
    for start, endpoints in data.items():
        for end, distance in endpoints.items():
            route_id = f"Route-{start}-{end}"
            map_graph.construct_route(start, end, route_id, distance)

    # Run predefined scenarios to test the map graph.
    run_test_cases(map_graph)


# Ensures that the main function is called only when the script is executed directly, not when imported.
if __name__ == "__main__":
    main()