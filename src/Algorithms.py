from abc import ABC, abstractmethod
from BuildGraph import BuildGraph
from Graph import Graph
import sys
import math
#change


#-------------------- STRATEGY ALGORITHMS ----------------------------------------
class graphAlgoStrategy(ABC):
   @abstractmethod
   #call with adj_list from graph
   def execute(self, graph, start, end):
     pass


class dijkstraStrategy:
    def execute(self, graph, start_node, end_node):
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

    
class AStarStrategy:

    def h(self,graph, s1, s2) -> float:
        lat1 = graph.get_node_loc(s1)[0]
        long1 = graph.get_node_loc(s1)[1]
        lat2 = graph.get_node_loc(s2)[0]
        long2 = graph.get_node_loc(s2)[1]

         # distance between in km
        return 6378.8*math.acos((math.sin(lat1) * math.sin(lat2)) + math.cos(lat1) * math.cos(lat2) * math.cos(long2-long1))

    def execute(self, graph, start, stop):
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
                if n == None or poo[v] + self.h(graph, v, stop) < poo[n] +self.h(graph, n, stop):
                    n = v

            if n == None:
                print('Path does not exist!')
                return None, None

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
                return reconst_path, None

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
        return None, None

    

#-------------------- STRATEGY ALGORITHMS ----------------------------------------





#Print -------------->
def dijkstra_print_result(previous_nodes, shortest_path, start_node, target_node):
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
        #print(" -> ".join(reversed(str(path))))



# --------Calling ALgo Strategy -----------------
app = BuildGraph()
graph = app.build_graph()

start = 1 #how do we figure out what we start at
stop = 286

def process_graph(processingStrategy: graphAlgoStrategy):
   prevNodes, shortestPath = processingStrategy.execute(graph,start,stop)
   return prevNodes, shortestPath

   
print("A STAR ---------------------------------------------")
#needed to add a second variable to fit strategy pattern
shortest_path, nothing = process_graph(AStarStrategy())


print("Dijkstra ---------------------------------------------")
previous_nodes, shortest_path = process_graph(dijkstraStrategy())
dijkstra_print_result(previous_nodes, shortest_path, 1, 286)




































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
