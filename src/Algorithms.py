from abc import ABC, abstractmethod
import sys
import math


# -------------------- STRATEGY ALGORITHMS ----------------------------------------
class GraphAlgoInterface(ABC):
    station = int
    time = int
    stations = [station]
    path = (stations, time)

    @abstractmethod
    def __init__(self, graph, start, end):
        """Initialize local variables"""
        pass

    @abstractmethod
    def execute(self) -> path:
        """Execute algorithm"""
        pass

    # @abstractmethod
    # def get_path(self):
    #     """Obtain result"""
    #     pass


class dijkstraStrategy(GraphAlgoInterface):
    station = int
    time = int
    stations = [station]
    path = (stations, time)

    def __init__(self, graph, start, end):
        self.graph = graph
        self.start = start
        self.end = end

    def execute(self) -> path:
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
                if current_min_node == None:
                    current_min_node = node
                elif shortest_path[node] < shortest_path[current_min_node]:
                    current_min_node = node

            # The code block below retrieves the current node's neighbors and updates their distances
            neighbors = self.graph.get_neighbors(current_min_node)
            for neighbor in neighbors:
                tentative_value = shortest_path[current_min_node] + \
                    self.graph.value(current_min_node, neighbor)
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
        return self.get_path(previous_nodes, shortest_path)

    def get_path(self, previous_nodes, shortest_path):
        path = []
        node = self.end

        while node != self.start:
            path.append(node)
            node = previous_nodes[node]

        # Add the start node manually
        path.append(self.start)

        return (list(reversed(path)), shortest_path[self.end])
        # print("We found the following best path with a value of {}.".format(
        #     shortest_path[self.end]))
        # for i in range(len(path)-1, 0, -1):
        #     print(path[i], "->", end=' ')
        # print(path[0])
        #print(" -> ".join(reversed(str(path))))


class AStarStrategy(GraphAlgoInterface):

    station = int
    time = int
    stations = [station]
    path = (stations, time)

    def __init__(self, graph, start, end):
        self.graph = graph
        self.start = start
        self.end = end

    def get_path_value(self, path) -> time:
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
                if n == None or poo[v] + self.h(v, self.end) < poo[n] + self.h(n, self.end):
                    n = v

            if n == None:
                print('Path does not exist!')
                return (None, None)

            # if the current node is the stop
            # then we start again from start
            if n == self.end:
                reconst_path = []

                while par[n] != n:
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
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
                    poo[m] = poo[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update par data and poo data
                # and if the node was in the closed_lst, move it to open_lst
                else:
                    if poo[m] > poo[n] + weight:
                        poo[m] = poo[n] + weight
                        par[m] = n

                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)

            # remove n from the open_lst, and add it to closed_lst
            # because all of his neighbors were inspected
            open_lst.remove(n)
            closed_lst.add(n)

        print('Path does not exist!')
        return (None, None)
