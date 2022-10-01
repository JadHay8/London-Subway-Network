from abc import ABC, abstractmethod
import sys
import math
#from Itinerary import Itinerary


# -------------------- STRATEGY ALGORITHMS ----------------------------------------
class GraphAlgoInterface(ABC):
    station = int
    time = int
    stations = [station]
    path = (stations, time)

    @abstractmethod
    def execute(self, graph, start, end) -> path:
        """Execute algorithm"""
        pass

    # @abstractmethod
    # def get_path(self):
    #     """Obtain result"""
    #     pass


class DijkstraStrategy(GraphAlgoInterface):
    station = int
    time = int
    stations = [station]
    path = (stations, time)

    def __init__(self):
        self.count = 0

    def execute(self, graph, start, end) -> path:
        # Source: https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html
        unvisited_nodes = list(range(1, graph.get_nodes()))

        shortest_path = {}
        previous_nodes = {}
        # We'll use max_value to initialize the "infinity" value of the unvisited nodes
        max_value = sys.maxsize
        for node in unvisited_nodes:
            shortest_path[node] = max_value
        # However, we initialize the starting node's value with 0
        shortest_path[start] = 0

        while unvisited_nodes:
            current_min_node = None
            for node in unvisited_nodes:  # Iterate over the nodes
                if current_min_node == None:
                    current_min_node = node
                    self.count += 1
                elif shortest_path[node] < shortest_path[current_min_node]:
                    current_min_node = node
                    self.count += 1

            # The code block below retrieves the current node's neighbors and updates their distances
            neighbors = graph.get_neighbors(current_min_node)
            for neighbor in neighbors:
                tentative_value = shortest_path[current_min_node] + \
                    graph.value(current_min_node, neighbor)

                # check if new station switches lines, if so add time
                if (graph.get_node_line(current_min_node) != graph.get_node_line(neighbor)):
                    tentative_value += 1

                if tentative_value < shortest_path[neighbor]:
                    shortest_path[neighbor] = tentative_value
                    # We also update the best path to the current node
                    previous_nodes[neighbor] = current_min_node
                    self.count += 1

            unvisited_nodes.remove(current_min_node)

        # print("previous nodes:", previous_nodes)
        # print("END")
        # print("shortest_path:", shortest_path)
        # print("END")
        # check shortest_path cost to 189
        return self.get_path(previous_nodes, shortest_path, start, end)

    def get_path(self, previous_nodes, shortest_path, start, end):
        path = []
        node = end

        while node != start:
            path.append(node)
            if end in previous_nodes:
                node = previous_nodes[node]
                self.count += 1
            else:
                print("no paths exists")
                self.count += 1
                return (None, None), self.count

        # Add the start node manually
        path.append(start)

        return (list(reversed(path)), shortest_path[end]), self.count
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

    def __init__(self):
        self.count = 0

    def get_path_value(self, path, graph) -> time:
        """get the total time/weight for the entire path"""
        return sum(graph.value(path[i], path[i+1]) for i in range(len(path)-1))

    def h(self, s1, s2, graph) -> float:
        lat1 = graph.get_node_loc(s1)[0]
        long1 = graph.get_node_loc(s1)[1]
        lat2 = graph.get_node_loc(s2)[0]
        long2 = graph.get_node_loc(s2)[1]

        # distance between in km
        return 6378.8*math.acos((math.sin(lat1) * math.sin(lat2)) + math.cos(lat1) * math.cos(lat2) * math.cos(long2-long1))

    def execute(self, graph, start, end) -> path:
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
                # if nodes have different lines then add weighting
                w = 0
                if (n != None) and (graph.get_node_line(n) != graph.get_node_line(v)):
                    w = 1
                if n == None or poo[v] + self.h(v, end, graph) + w < poo[n] + self.h(n, end, graph) + w:
                    n = v
                    self.count += 1

            if n == None:
                print('Path does not exist!')
                self.count += 1
                return (None, None), self.count

            # if the current node is the stop
            # then we start again from start
            if n == end:
                self.count += 1
                reconst_path = []

                while par[n] != n:
                    reconst_path.append(n)
                    n = par[n]

                reconst_path.append(start)

                reconst_path.reverse()

                value = self.get_path_value(reconst_path, graph)

                #print('Path found: {}'.format(reconst_path))
                return (reconst_path, value), self.count

            # for all the neighbors of the current node do
            for m in graph.get_neighbors(n):
                weight = graph.value(n, m)

                # if there is a line transfer between nodes add weight as well:
                if graph.get_node_line(n) != graph.get_node_line(m):
                    weight += 1

                # if the current node is not presentin both open_lst and closed_lst
                # add it to open_lst and note n as it's par
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
                    poo[m] = poo[n] + weight
                    self.count += 1

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update par data and poo data
                # and if the node was in the closed_lst, move it to open_lst
                else:
                    if poo[m] > poo[n] + weight:
                        poo[m] = poo[n] + weight
                        par[m] = n
                        self.count += 1

                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)
                            self.count += 1

            # remove n from the open_lst, and add it to closed_lst
            # because all of his neighbors were inspected
            open_lst.remove(n)
            closed_lst.add(n)

        print('Path does not exist!')
        return (None, None), self.count


# -------------------- STRATEGY ALGORITHMS ----------------------------------------


# ------------------------------- Original Algorithms ----------------------------->


# class Algorithms:

#     def dijkstra(self,graph, start_node):
#         # Source: https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html
#         unvisited_nodes = list(range(graph.get_nodes()))

#         shortest_path = {}
#         previous_nodes = {}
#         # We'll use max_value to initialize the "infinity" value of the unvisited nodes
#         max_value = sys.maxsize
#         for node in unvisited_nodes:
#             shortest_path[node] = max_value
#         # However, we initialize the starting node's value with 0
#         shortest_path[start_node] = 0

#         while unvisited_nodes:
#             current_min_node = None
#             for node in unvisited_nodes:  # Iterate over the nodes
#                 if current_min_node == None:
#                     current_min_node = node
#                 elif shortest_path[node] < shortest_path[current_min_node]:
#                     current_min_node = node

#             # The code block below retrieves the current node's neighbors and updates their distances
#             neighbors = graph.get_neighbors(current_min_node)
#             for neighbor in neighbors:
#                 tentative_value = shortest_path[current_min_node] + \
#                     graph.value(current_min_node, neighbor)
#                 if tentative_value < shortest_path[neighbor]:
#                     shortest_path[neighbor] = tentative_value
#                     # We also update the best path to the current node
#                     previous_nodes[neighbor] = current_min_node

#             unvisited_nodes.remove(current_min_node)

#         return previous_nodes, shortest_path


#     def dijkstra_print_result(self,previous_nodes, shortest_path, start_node, target_node):
#         path = []
#         node = target_node

#         while node != start_node:
#             path.append(node)
#             node = previous_nodes[node]

#         # Add the start node manually
#         path.append(start_node)

#         print("We found the following best path with a value of {}.".format(
#             shortest_path[target_node]))
#         for i in range(len(path)-1, 0, -1):
#             print(path[i], "->", end=' ')
#         print(path[0])
#         # print(" -> ".join(reversed(str(path))))


# # ------------------------ A* ---------------------------------------------------------------
#     def h(self,graph, s1, s2) -> float:
#         lat1 = graph.get_node_loc(s1)[0]
#         long1 = graph.get_node_loc(s1)[1]
#         lat2 = graph.get_node_loc(s2)[0]
#         long2 = graph.get_node_loc(s2)[1]

#     # distance between in km
#         return 6378.8*math.acos((math.sin(lat1) * math.sin(lat2)) + math.cos(lat1) * math.cos(lat2) * math.cos(long2-long1))


#     def a_star_algorithm(self,graph, start, stop):

#         # Source: https://www.pythonpool.com/a-star-algorithm-python/#:~:text=A*%20Algorithm%20in%20Python%20or,a%20wide%20range%20of%20contexts.

#         # In this open_lst is a list of nodes which have been visited, but who's
#         # neighbours haven't all been always inspected, It starts off with the start
#         # node
#         # And closed_lst is a list of nodes which have been visited
#         # and who's neighbors have been always inspected
#         open_lst = set([start])
#         closed_lst = set([])

#         # poo has present distances from start to all other nodes
#         # the default value is +infinity
#         poo = {}
#         poo[start] = 0

#         # par contains an adjac mapping of all nodes
#         par = {}
#         par[start] = start

#         while len(open_lst) > 0:
#             n = None

#             # it will find a node with the lowest value of f() -
#             for v in open_lst:
#                 if n == None or poo[v] + self.h(graph, v, stop) < poo[n] +self.h(graph, n, stop):
#                     n = v

#             if n == None:
#                 print('Path does not exist!')
#                 return None

#             # if the current node is the stop
#             # then we start again from start
#             if n == stop:
#                 reconst_path = []

#                 while par[n] != n:
#                     reconst_path.append(n)
#                     n = par[n]

#                 reconst_path.append(start)

#                 reconst_path.reverse()

#                 print('Path found: {}'.format(reconst_path))
#                 return reconst_path

#             # for all the neighbors of the current node do
#             for m in graph.get_neighbors(n):
#                 weight = graph.value(n, m)
#                 # if the current node is not presentin both open_lst and closed_lst
#                 # add it to open_lst and note n as it's par
#                 if m not in open_lst and m not in closed_lst:
#                     open_lst.add(m)
#                     par[m] = n
#                     poo[m] = poo[n] + weight

#                 # otherwise, check if it's quicker to first visit n, then m
#                 # and if it is, update par data and poo data
#                 # and if the node was in the closed_lst, move it to open_lst
#                 else:
#                     if poo[m] > poo[n] + weight:
#                         poo[m] = poo[n] + weight
#                         par[m] = n

#                         if m in closed_lst:
#                             closed_lst.remove(m)
#                             open_lst.add(m)

#             # remove n from the open_lst, and add it to closed_lst
#             # because all of his neighbors were inspected
#             open_lst.remove(n)
#             closed_lst.add(n)

#         print('Path does not exist!')
#         return None
