import heapq


# Represents a connection between two points in the graph.
class Connection:
    def __init__(self, route_id, distance):
        self.route_id = route_id
        self.distance = distance
