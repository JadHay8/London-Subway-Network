import sys
from Graph import Graph
import math
from Algorithms import *
import pyperf

# time, data accesses,


class DijkstraComparisons(GraphAlgoInterface):

    def __init__(self, graph, start, end):
        self.graph = graph
        self.start = start
        self.end = end
        self.count = 0

    def execute(self):
        # Source: https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html
        unvisited_nodes = list(range(1, self.graph.get_nodes()))

        shortest_path = {}
        previous_nodes = {}
        # We'll use max_value to initialize the "infinity" value of the unvisited nodes
        max_value = sys.maxsize
        for node in unvisited_nodes:
            shortest_path[node] = max_value
        # However, we initialize the starting node's value with 0
        shortest_path[self.start] = 0

        while unvisited_nodes:
            current_min_node = None
            for node in unvisited_nodes:  # Iterate over the nodes
                self.count += 1
                if current_min_node == None:
                    current_min_node = node
                elif shortest_path[node] < shortest_path[current_min_node]:
                    self.count += 1
                    current_min_node = node

            # The code block below retrieves the current node's neighbors and updates their distances
            neighbors = self.graph.get_neighbors(current_min_node)
            for neighbor in neighbors:
                tentative_value = shortest_path[current_min_node] + \
                    self.graph.value(current_min_node, neighbor)
                self.count += 1
                if tentative_value < shortest_path[neighbor]:
                    shortest_path[neighbor] = tentative_value
                    # We also update the best path to the current node
                    previous_nodes[neighbor] = current_min_node

            unvisited_nodes.remove(current_min_node)

        # print("previous nodes:", previous_nodes)
        # print("END")
        # print("shortest_path:", shortest_path)
        # print("END")
        # check shortest_path cost to 189
        return self.get_path(previous_nodes)

    def get_path(self, previous_nodes):
        path = []
        node = self.end

        self.count += 1
        while node != self.start:
            self.count += 1
            path.append(node)
            node = previous_nodes[node]

        # Add the start node manually
        path.append(self.start)

        return list(reversed(path))

    def get_count(self):
        return self.count


class AStarStrategy(GraphAlgoInterface):

    station = int
    time = int
    stations = [station]
    path = (stations, time)

    def __init__(self, graph, start, end):
        self.graph = graph
        self.start = start
        self.end = end
        self.count = 0

    def get_path_value(self, path) -> int:
        """get the total time/weight for the entire path"""
        return sum(self.graph.value(path[i], path[i+1]) for i in range(len(path)-1))

    def h(self, s1, s2) -> float:
        lat1 = self.graph.get_node_loc(s1)[0]
        long1 = self.graph.get_node_loc(s1)[1]
        lat2 = self.graph.get_node_loc(s2)[0]
        long2 = self.graph.get_node_loc(s2)[1]

        # distance between in km
        return 6378.8*math.acos((math.sin(lat1) * math.sin(lat2)) + math.cos(lat1) * math.cos(lat2) * math.cos(long2-long1))

    def execute(self) -> path:
        # Source: https://www.pythonpool.com/a-star-algorithm-python/#:~:text=A*%20Algorithm%20in%20Python%20or,a%20wide%20range%20of%20contexts.

        # In this open_lst is a list of nodes which have been visited, but who's
        # neighbours haven't all been always inspected, It starts off with the start
        # node
        # And closed_lst is a list of nodes which have been visited
        # and who's neighbors have been always inspected
        open_lst = set([self.start])
        closed_lst = set([])

        # poo has present distances from start to all other nodes
        # the default value is +infinity
        poo = {}
        poo[self.start] = 0

        # par contains an adjac mapping of all nodes
        par = {}
        par[self.start] = self.start

        while len(open_lst) > 0:
            n = None

            # it will find a node with the lowest value of f() -
            for v in open_lst:
                self.count += 1
                if n == None or poo[v] + self.h(v, self.end) < poo[n] + self.h(n, self.end):
                    n = v

            self.count += 1
            if n == None:
                print('Path does not exist!')
                return (None, None)

            # if the current node is the stop
            # then we start again from start
            self.count += 1
            if n == self.end:
                reconst_path = []

                self.count += 1
                while par[n] != n:
                    self.count += 1
                    reconst_path.append(n)
                    n = par[n]

                reconst_path.append(self.start)

                reconst_path.reverse()

                value = self.get_path_value(reconst_path)

                print('Path found: {}'.format(reconst_path))
                return (reconst_path, value)

            # for all the neighbors of the current node do
            for m in self.graph.get_neighbors(n):
                weight = self.graph.value(n, m)
                # if the current node is not presentin both open_lst and closed_lst
                # add it to open_lst and note n as it's par
                self.count += 1
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
                    poo[m] = poo[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update par data and poo data
                # and if the node was in the closed_lst, move it to open_lst
                else:
                    self.count += 1
                    if poo[m] > poo[n] + weight:
                        poo[m] = poo[n] + weight
                        par[m] = n

                        self.count += 1
                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)

            # remove n from the open_lst, and add it to closed_lst
            # because all of his neighbors were inspected
            open_lst.remove(n)
            closed_lst.add(n)

        print('Path does not exist!')
        return (None, None)

    def get_count(self):
        return self.count


def test_dijkstra():

    graph = Graph(10)

    graph.add_edge(1, 2, 4)
    graph.add_edge(4, 2, 2)
    graph.add_edge(8, 3, 7)
    graph.add_edge(5, 6, 2)
    graph.add_edge(8, 9, 3)
    graph.add_edge(4, 9, 4)
    graph.add_edge(6, 3, 1)  # find 1,8 path

    x = DijkstraComparisons(graph, 1, 8)
    x.execute()
    return x.get_count()


def test_AStar():

    graph = Graph(10)

    graph.add_edge(1, 2, 4)
    graph.add_edge(4, 2, 2)
    graph.add_edge(8, 3, 7)
    graph.add_edge(5, 6, 2)
    graph.add_edge(8, 9, 3)
    graph.add_edge(4, 9, 4)
    graph.add_edge(6, 3, 1)  # find 1,8 path

    x = AStarStrategy(graph, 1, 8)
    x.execute()
    return x.get_count()


print("Dijkstra Comparisons:", test_dijkstra())
print("AStar Comparisons:", test_AStar())
