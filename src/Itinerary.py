from Algorithms.AlgorithmsStrategy import *
from Graphing.BuildGraph import *


class Itinerary:
    #Alias
    path = [int]

    def __init__(self, graph, station1, station2):
        self.graph = graph
        self.station1 = station1
        self.station2 = station2

    def get_itinerary(self) -> tuple[path,path]:
        '''
        get shortest paths from either algorithm - number of line transfers already factored in.
        '''

        shortest_path_dijk = DijkstraStrategy().execute(
            self.graph, self.station1, self.station2)

        shortest_path_AStar = AStarStrategy().execute(
            self.graph, self.station1, self.station2)

        return shortest_path_AStar,shortest_path_dijk


graph = BuildGraph().build_graph()
it = Itinerary(graph, 1, 10)
print(it.get_itinerary()[0])
print(it.get_itinerary()[1])
# graph = Graph(10)
# #graph.add_edge(0, 0, 4,1)
# graph.add_edge(1, 2, 4, 1)
# graph.add_edge(2, 3, 2, 2)
# graph.add_edge(3, 4, 7, 3)
# graph.add_edge(4, 8, 2, 4)
# graph.add_edge(1, 5, 4, 1)
# graph.add_edge(5, 6, 2, 1)
# graph.add_edge(6, 7, 7, 1)
# graph.add_edge(7, 8, 2, 1)
