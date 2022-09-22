
class Graph:
    def __init__(self, num_of_nodes, directed=False):
        self.m_num_of_nodes = num_of_nodes
        self.m_nodes = range(self.m_num_of_nodes)

        # Define the type of a graph
        self.m_directed = directed

        self.node_loc = {node: [] for node in self.m_nodes}
        self.m_adj_list = {node: set() for node in self.m_nodes}

# ---------------------adj_list-----------------------------------------
    def add_edge(self, node1, node2, weight):
        self.m_adj_list[node1].add((node2, weight))

        if not self.m_directed:
            self.m_adj_list[node2].add((node1, weight))

    def get_nodes(self):
        return self.m_num_of_nodes

    def get_adjList(self):
        return self.m_adj_list

    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        for tuple in self.m_adj_list.get(node1):
            if tuple[0] == node2:
                return tuple[1]

    def get_neighbors(self, node):
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

# ---------------------adj_list-----------------------------------------


# ---------------------node_loc-----------------------------------------


    def add_node_loc(self, node, long, lat):
        self.node_loc[node].append((long, lat))

    def get_node_loc(self, station):
        return self.node_loc.get(station)[0]
    
    def get_node_dist(self):
        return self.m_nodes

    def print_node_loc(self):
        for key in self.node_loc.keys():
            print("node", key, ": ", self.node_loc[key])
        print("end node dist \n")

# ---------------------node_loc-----------------------------------------

# Source: https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/representing-graphs-in-code/

    # graph.print_adj_list()
    # graph.print_node_loc()
    # print(graph.get_node_loc(7))

