from Graph import Graph
from Graph import BuildGraph
import sys
import csv
import math


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

    def numTransfers(self, station):
        return len(station)-1

    def getItinerary(self):
        '''
        get shortest path and rank to get the number 1 best path
        '''
        TODO
        pass


def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node

    while node != start_node:
        path.append(node)
        node = previous_nodes[node]

    # Add the start node manually
    path.append(start_node)

    print("We found the following best path with a value of {}.".format(
        shortest_path[target_node]))
    for i in range(len(path)-1, 0, -1):
        print(path[i], "->", end=' ')
    print(path[0])
    # print(" -> ".join(reversed(str(path))))


def dijkstra(graph, start_node):
    # Source: https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html
    unvisited_nodes = list(range(graph.get_nodes()))

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
        neighbors = graph.get_neighbors(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + \
                graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node

        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path


def test():
    with open('_dataset/london.stations.csv') as file:
        stations = csv.reader(file)

        # row count other than first line of headers is number of stations
        numStations = sum(1 for row in stations)+1

        graph = Graph(numStations)

        with open('_dataset/london.connections.csv') as file2:
            connections = csv.reader(file2)
            for fileLine in connections:
                if connections.line_num != 1:
                    graph.add_edge(int(fileLine[0]), int(
                        fileLine[1]), int(fileLine[3]))

    # graph.print_adj_list()

    # graph = Graph(10)
    # graph.add_edge(1, 2, 3)
    # graph.add_edge(5, 3, 2)
    # graph.add_edge(8, 4, 6)
    # graph.add_edge(8, 7, 2)
    # graph.add_edge(9, 7, 1)
    # graph.add_edge(9, 8, 3)
    # graph.add_edge(6, 0, 2)

    # graph.print_adj_list()

    previous_nodes, shortest_path = dijkstra(graph, 1)

    print_result(previous_nodes, shortest_path, 1, 286)

# test()


def h(graph, s1, s2) -> float:
    # print("here", graph.get_node_loc(4)[0][0])
    # print("h", s1, s2)
    lat1 = graph.get_node_loc(s1)[0]
    long1 = graph.get_node_loc(s1)[1]
    lat2 = graph.get_node_loc(s2)[0]
    long2 = graph.get_node_loc(s2)[1]

    # distance between in km
    return 6378.8*math.acos((math.sin(lat1) * math.sin(lat2)) + math.cos(lat1) * math.cos(lat2) * math.cos(long2-long1))


def a_star_algorithm(graph, start, stop):

    # Source: https://www.pythonpool.com/a-star-algorithm-python/#:~:text=A*%20Algorithm%20in%20Python%20or,a%20wide%20range%20of%20contexts.

    # In this open_lst is a list of nodes which have been visited, but who's
    # neighbours haven't all been always inspected, It starts off with the start
    # node
    # And closed_lst is a list of nodes which have been visited
    # and who's neighbors have been always inspected
    open_lst = set([start])
    closed_lst = set([])

    # poo has present distances from start to all other nodes
    # the default value is +infinity
    poo = {}
    poo[start] = 0

    # par contains an adjac mapping of all nodes
    par = {}
    par[start] = start

    while len(open_lst) > 0:
        n = None

        # it will find a node with the lowest value of f() -
        for v in open_lst:
            if n == None or poo[v] + h(graph, v, stop) < poo[n] + h(graph, n, stop):
                n = v

        if n == None:
            print('Path does not exist!')
            return None

        # if the current node is the stop
        # then we start again from start
        if n == stop:
            reconst_path = []

            while par[n] != n:
                reconst_path.append(n)
                n = par[n]

            reconst_path.append(start)

            reconst_path.reverse()

            print('Path found: {}'.format(reconst_path))
            return reconst_path

        # for all the neighbors of the current node do
        for m in graph.get_neighbors(n):
            weight = graph.value(n, m)
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
    return None


def test_a_star():
    # graph = Graph(10)
    # graph.add_edge(1, 2, 3)
    # graph.add_edge(5, 3, 2)
    # graph.add_edge(8, 4, 6)
    # graph.add_edge(8, 7, 2)
    # graph.add_edge(9, 7, 1)
    # graph.add_edge(9, 8, 3)
    # graph.add_edge(6, 0, 2)

    with open('_dataset/london.stations.csv') as file:
        stations = csv.reader(file)

        graph = Graph(1+sum(1 for row in stations))

        # Go back to beginning of file by reopening

        with open('_dataset/london.stations.csv') as filee:
            stationss = csv.reader(filee)
            for fileLine in stationss:
                if stationss.line_num != 1:
                    graph.add_node_loc(float(fileLine[0]), float(
                        fileLine[1]), float(fileLine[2]))

        with open('_dataset/london.connections.csv') as file2:
            connections = csv.reader(file2)
            for fileLine in connections:
                # print(fileLine)
                if connections.line_num != 1:
                    graph.add_edge(int(fileLine[0]), int(
                        fileLine[1]), int(fileLine[3]))

    # graph.print_adj_list()
        # print("hey", graph.get_node_loc(1))

    a_star_algorithm(graph, 1, 286)


with open('_dataset/london.connections.csv') as file2:
    connections = csv.reader(file2)
app = BuildGraph(file, file2)
graph = app.build_graph()

a_star_algorithm(graph, 1, 286)
