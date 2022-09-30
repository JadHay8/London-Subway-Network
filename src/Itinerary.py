from Algorithms.AlgorithmsStrategy import *
from Graphing.BuildGraph import *


class Itinerary:
    def __init__(self, graph, station1, station2):
        self.graph = graph
        self.station1 = station1
        self.station2 = station2

    def rankPaths(self, path1, path2):
        """"This is called if time of path 1 is the same as time of path 2"""

        if self.numTransfers(path1) > self.numTransfers(path2):
            return path2
        else:
            return path1

    def numTransfers(self, path1, path2):
        transfers = 0
        for station in path1:
            station = 1
        return len(path1)-1

    # def get_itinerary(self):
    #     '''
    #     get shortest path and rank to get the number 1 best path
    #     '''

    #     shortest_path_dijk = process_graph(dijkstraStrategy(
    #         self.graph, self.station1, self.station2))
    #     shortest_path_AStar = process_graph(
    #         AStarStrategy(self.graph, self.station1, self.station2))

    #     if shortest_path_dijk[1] == shortest_path_AStar[1]:
    #         return self.rankPaths(shortest_path_dijk[0], shortest_path_AStar[0])

    #     print("Both paths are the same.")
    #     return shortest_path_dijk[0]


graph = Graph(10)
#graph.add_edge(0, 0, 4,1)
graph.add_edge(1, 2, 4, 1)
graph.add_edge(2, 3, 2, 2)
graph.add_edge(3, 4, 7, 3)
graph.add_edge(4, 8, 2, 4)
graph.add_edge(1, 5, 4, 1)
graph.add_edge(5, 6, 2, 1)
graph.add_edge(6, 7, 7, 1)
graph.add_edge(7, 8, 2, 1)

#


def process_graph(processingStrategy: GraphAlgoInterface):
    shortestPath = processingStrategy.execute()
    return shortestPath


print("Dijkstra ---------------------------------------------")
start = 1
stop = 8
shortest_path = process_graph(dijkstraStrategy(graph, start, stop))
print(shortest_path)

# test = Itinerary()

# test.numTransfers(self, shortest_path)

# graph.add_node_loc(1,1.4, 2.3)
# graph.add_node_loc(2,1, 2)
# graph.add_node_loc(3,1, 2)
# graph.add_node_loc(4,1, 2)
# graph.add_node_loc(5,1, 2)
# graph.add_node_loc(6,1, 2)
# graph.add_node_loc(7,1, 2)
# graph.add_node_loc(8, 1, 2)
