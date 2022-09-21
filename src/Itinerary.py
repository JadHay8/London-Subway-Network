from Graph import Graph
import sys
import csv


class Itinerary:
    def __init__(self, graph, station1, station2):
        self.graph = graph
        self.station1 = station1
        self.station2 = station2

    def rankPaths(self, path1, path2):
        pass
        # if length(path1) == length(path2):
        #   whichever has less transfers
        # otherwise: if shortestPath(path1,path2) == path1: return path1 else return path2

    def numTransfers(self, other):
        TODO
        pass

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
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + \
                graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node

        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path


# def test():
#     with open('_dataset/london.stations.csv') as file:
#         stations = csv.reader(file)

#         # row count other than first line of headers is number of stations
#         numStations = sum(1 for row in stations)+1

#         graph = Graph(numStations)

#         with open('_dataset/london.connections.csv') as file2:
#             connections = csv.reader(file2)
#             for fileLine in connections:
#                 if connections.line_num != 1:
#                     graph.add_edge(int(fileLine[0]), int(
#                         fileLine[1]), int(fileLine[3]))

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


# def h(n):
#         H = {
#             'A': 1,
#             'B': 1,
#             'C': 1,
#             'D': 1
#         }

#         return H[n]


def a_star_algorithm(start, stop):

    # Source: https://www.pythonpool.com/a-star-algorithm-python/#:~:text=A*%20Algorithm%20in%20Python%20or,a%20wide%20range%20of%20contexts.

    # In this open_lst is a lisy of nodes which have been visited, but who's
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
            if n == None or poo[v] + self.h(v) < poo[n] + self.h(n):
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
        for (m, weight) in self.get_neighbors(n):
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
