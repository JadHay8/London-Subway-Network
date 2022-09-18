from Graph import Graph
import sys


class Itinerary:
    def __init__(self, graph, station1, station2):
        self.graph = graph
        self.station1 = station1
        self.station2 = station2

    def rankPaths(self, path1, path2):
        # if length(path1) == length(path2):
        #   whichever has less transfers
        # otherwise: if shortestPath(path1,path2) == path1: return path1 else return path2

    def dijkstra(self, graph, start_node) -> list[int]:
        unvisited_nodes = list(graph.get_nodes())

        shortest_path = {}
        previous_nodes = {}
        # We'll use max_value to initialize the "infinity" value of the unvisited nodes
        max_value = sys.maxsize
        for node in unvisited_nodes:
            shortest_path[node] = max_value
        # However, we initialize the starting node's value with 0
        shortest_path[start_node] = 0

        while unvisited_nodes:
            current_min_node = None
            for node in unvisited_nodes:  # Iterate over the nodes
                if current_min_node == None:
                    current_min_node = node
                elif shortest_path[node] < shortest_path[current_min_node]:
                    current_min_node = node

                # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + \
                graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node

    def numTransfers(self, other):
        TODO
        pass

    def getItinierary(self):
        '''
        get shortest path and rank to get the number 1 best path
        '''
        TODO
        pass


itinerary1 = Itinerary(Graph, station1, station2)
itinerary1.getItinerary()

'''
node 0: {(10,2),(100,4),...}
node 1: {(120,2),(101,3),...}
.
.
.
'''
