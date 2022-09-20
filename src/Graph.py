import csv


class Graph:
    def __init__(self, num_of_nodes, directed=False):
        self.m_num_of_nodes = num_of_nodes
        self.m_nodes = range(self.m_num_of_nodes)

        # Define the type of a graph
        self.m_directed = directed

        self.m_adj_list = {node: set() for node in self.m_nodes}

    def add_edge(self, node1, node2, weight):
        self.m_adj_list[node1].add((node2, weight))

        if not self.m_directed:
            self.m_adj_list[node2].add((node1, weight))

    def get_nodes(self):
        return self.m_num_of_nodes

    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        for tuple in self.m_adj_list.get(node1):
            if tuple[0] == node2:
                return tuple[1]

    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        # append all neighbours of node
        for tuple in self.m_adj_list.get(node):
            connections.append(tuple[0])

        return connections

    def print_adj_list(self):
        # print(self.m_adj_list.get(1))
        # print("adjacency list: \t", self.m_adj_list)
        for key in self.m_adj_list.keys():
            print("node", key, ": ", self.m_adj_list[key])
        print("end adj list \n")

# Source: https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/representing-graphs-in-code/


# graph = Graph(5)

# graph.add_edge(0, 0, 25)
# graph.add_edge(0, 1, 5)
# graph.add_edge(0, 2, 3)
# graph.add_edge(1, 3, 1)
# graph.add_edge(1, 4, 15)
# graph.add_edge(4, 2, 7)
# graph.add_edge(4, 3, 11)
# graph.print_adj_list()

# with open('_dataset/london.stations.csv') as file:
#     stations = csv.reader(file)

#     # row count other than first line of headers is number of stations
#     numStations = sum(1 for row in stations)+1

#     graph = Graph(numStations)

#     with open('_dataset/london.connections.csv') as file2:
#         connections = csv.reader(file2)
#         for fileLine in connections:
#             if connections.line_num != 1:
#                 graph.add_edge(int(fileLine[0]), int(
#                     fileLine[1]), int(fileLine[3]))

#     graph.print_adj_list()
