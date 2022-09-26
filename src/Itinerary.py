from Algorithms import *
from BuildGraph import *


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

    def numTransfers(self, path):
        return len(path)-1

    def get_itinerary(self):
        '''
        get shortest path and rank to get the number 1 best path
        '''

        shortest_path_dijk = process_graph(dijkstraStrategy(
            self.graph, self.station1, self.station2))
        shortest_path_AStar = process_graph(
            AStarStrategy(self.graph, self.station1, self.station2))

        if shortest_path_dijk[1] == shortest_path_AStar[1]:
            return self.rankPaths(shortest_path_dijk[0], shortest_path_AStar[0])

        print("Both paths are the same.")
        return shortest_path_dijk[0]

    def process_graph(processingStrategy: GraphAlgoInterface):
        shortestPath = processingStrategy.execute()
        return shortestPath
