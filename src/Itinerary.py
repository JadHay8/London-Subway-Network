from Algorithms import Algorithm

from Algorithms import Algorithm


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
        a = Algorithm()
        path = a.a_star_algorithm(self.graph, self.station1, self.station2)

        print("path: ", path)
        return path
