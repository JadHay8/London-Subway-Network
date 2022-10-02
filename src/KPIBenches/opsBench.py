import sys
import math
from Algorithms.AlgorithmsStrategy import GraphAlgoInterface


class DijkstraOps(GraphAlgoInterface):
    opsCounter = int
    opsCounter = 0
    
    def _ops(self):
      self.opsCounter  += 1
    def get_ops(self) -> int:
      return self.opsCounter

    def execute(self,graph, start, end) -> opsCounter:
        # Source: https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html
        unvisited_nodes = list(range(1, graph.get_nodes()))
        self._ops()

        shortest_path = {}
        previous_nodes = {}
        # We'll use max_value to initialize the "infinity" value of the unvisited nodes
        max_value = sys.maxsize
        for node in unvisited_nodes:
            self._ops()
            shortest_path[node] = max_value
            self._ops()
        # However, we initialize the starting node's value with 0
        shortest_path[start] = 0

        while unvisited_nodes:
            self._ops()
            current_min_node = None
            for node in unvisited_nodes:  # Iterate over the nodes
                self._ops()
                if current_min_node == None:
                    self._ops()
                    current_min_node = node
                elif shortest_path[node] < shortest_path[current_min_node]:
                    self._ops()
                    current_min_node = node
                    #increment for data access in elif statement
                    self._ops()
                    self._ops()

            # The code block below retrieves the current node's neighbors and updates their distances
            neighbors = graph.get_neighbors(current_min_node)
            self._ops()
            for neighbor in neighbors:
                self._ops()
                tentative_value = shortest_path[current_min_node] + \
                    graph.value(current_min_node, neighbor)
                self._ops()
                self._ops()

                #check if new station switches lines, if so add time
                if (graph.get_node_line(current_min_node) != graph.get_node_line(neighbor)):
                    tentative_value += 1 
                    self._ops()
                    #account for data access in if statement
                    self._ops()
                    self._ops()

                if tentative_value < shortest_path[neighbor]:
                    self._ops()
                    self._ops()
                    shortest_path[neighbor] = tentative_value
                    self._ops()
                    # We also update the best path to the current node
                    previous_nodes[neighbor] = current_min_node
                    self._ops()

            unvisited_nodes.remove(current_min_node)
            self._ops()

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
            self._ops()
            path.append(node)
            self._ops()
            if end in previous_nodes:
                self._ops()
                node = previous_nodes[node]
                self._ops()
            else:
                print("no path exists")
                return self.get_ops()
            self._ops()

        # Add the start node manually
        path.append(start) 
        self._ops()
        print(list(reversed(path)), shortest_path[end])
        return self.get_ops()



class AStarOps(GraphAlgoInterface):

    opsCounter = int
    opsCounter = 0
    
    def _ops(self):
      self.opsCounter  += 1
    def get_ops(self) -> int:
      return self.opsCounter

    def get_path_value(self, path,graph) -> int:
        """get the total time/weight for the entire path"""
        for i in range(len(path)-1):
            self._ops()
        return sum(graph.value(path[i], path[i+1]) for i in range(len(path)-1))

    def h(self, s1, s2,graph) -> float:
        lat1 = graph.get_node_loc(s1)[0]
        self._ops()
        long1 = graph.get_node_loc(s1)[1]
        self._ops()
        lat2 = graph.get_node_loc(s2)[0]
        self._ops()
        long2 = graph.get_node_loc(s2)[1]
        self._ops()

        # distance between in km
        return 6378.8*math.acos((math.sin(lat1) * math.sin(lat2)) + math.cos(lat1) * math.cos(lat2) * math.cos(long2-long1))

    def execute(self, graph, start, end) -> opsCounter:
        # Source: https://www.pythonpool.com/a-star-algorithm-python/#:~:text=A*%20Algorithm%20in%20Python%20or,a%20wide%20range%20of%20contexts.

        # In this open_lst is a list of nodes which have been visited, but who's
        # neighbours haven't all been always inspected, It starts off with the start
        # node
        # And closed_lst is a list of nodes which have been visited
        # and who's neighbors have been always inspected
        open_lst = set([start])
        self._ops()
        closed_lst = set([])
        self._ops()

        # poo has present distances from start to all other nodes
        # the default value is +infinity
        poo = {}
        poo[start] = 0

        # par contains an adjac mapping of all nodes
        par = {}
        par[start] = start
        self._ops()

        while len(open_lst) > 0:
            self._ops()
            n = None

            # it will find a node with the lowest value of f() -
            for v in open_lst:
                self._ops()
                # if nodes have different lines then add weighting
                w = 0
                if (n != None) and (graph.get_node_line(n) != graph.get_node_line(v)):
                    w = 1
                    self._ops()
                    #account for data access and comparisons in if statment
                    self._ops()
                    self._ops()

                if n == None or poo[v] + self.h(v, end, graph) + w < poo[n] + self.h(n, end, graph) + w:
                    n = v
                    self._ops()
                    #account for data access and comparisons in if statment
                    self._ops()
                    self._ops()
                    self._ops()
                    self._ops()
            if n == None:
                self._ops()
                print('Path does not exist!')
                self._ops()
                return self.get_ops()

            # if the current node is the stop
            # then we start again from start
            if n == end:
                self._ops()
                reconst_path = []

                while par[n] != n:
                    self._ops()
                    reconst_path.append(n)
                    self._ops()
                    n = par[n]
                    self._ops()

                reconst_path.append(start)
                self._ops()

                reconst_path.reverse()
                self._ops()

                value = self.get_path_value(reconst_path, graph)
                self._ops()

                print('Path found: {}'.format(reconst_path, graph), value)
                return self.get_ops()

            # for all the neighbors of the current node do
            for m in graph.get_neighbors(n):
                self._ops()
                weight = graph.value(n, m)
                self._ops()
                # if the current node is not presentin both open_lst and closed_lst
                # add it to open_lst and note n as it's par
                if m not in open_lst and m not in closed_lst:
                    self._ops()
                    open_lst.add(m)
                    self._ops()
                    par[m] = n
                    self._ops()
                    poo[m] = poo[n] + weight
                    self._ops()

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update par data and poo data
                # and if the node was in the closed_lst, move it to open_lst
                else:
                    self._ops()
                    if poo[m] > poo[n] + weight:
                        self._ops()
                        poo[m] = poo[n] + weight
                        self._ops()
                        par[m] = n
                        self._ops()

                        if m in closed_lst:
                            self._ops()
                            closed_lst.remove(m)
                            self._ops()
                            open_lst.add(m)
                            self._ops()

            # remove n from the open_lst, and add it to closed_lst
            # because all of his neighbors were inspected
            open_lst.remove(n)
            self._ops()
            closed_lst.add(n)
            self._ops()

        print('Path does not exist!')
        return self.get_ops()





# def test_dijkstra():

#     graph = Graph(10)

#     graph.add_edge(1, 2, 4)
#     graph.add_edge(4, 2, 2)
#     graph.add_edge(8, 3, 7)
#     graph.add_edge(5, 6, 2)
#     graph.add_edge(8, 9, 3)
#     graph.add_edge(4, 9, 4)
#     graph.add_edge(6, 3, 1)  # find 1,8 path

#     x = DijkstraComparisons(graph, 1, 8)
#     x.execute()
#     return x.get_count()


# def test_AStar():

#     graph = Graph(10)

#     graph.add_edge(1, 2, 4)
#     graph.add_edge(4, 2, 2)
#     graph.add_edge(8, 3, 7)
#     graph.add_edge(5, 6, 2)
#     graph.add_edge(8, 9, 3)
#     graph.add_edge(4, 9, 4)
#     graph.add_edge(6, 3, 1)  # find 1,8 path

#     x = AStarStrategy(graph, 1, 8)
#     x.execute()
#     return x.get_count()


# print("Dijkstra Comparisons:", test_dijkstra())
# print("AStar Comparisons:", test_AStar())
