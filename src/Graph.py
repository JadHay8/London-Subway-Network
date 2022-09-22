import csv


class Graph:
    def __init__(self, num_of_nodes, directed=False):
        self.m_num_of_nodes = num_of_nodes
        self.m_nodes = range(self.m_num_of_nodes)

        # Define the type of a graph
        self.m_directed = directed

        self.node_dist = {node: set() for node in self.m_nodes}
        self.m_adj_list = {node: set() for node in self.m_nodes}
        
#---------------------adj_list-----------------------------------------
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

#---------------------adj_list-----------------------------------------  



#---------------------node_dist-----------------------------------------
   
    def add_node_dist(self, node, long, lat):
        self.node_dist[node].add((long,lat))

    def get_node_dist(self):
        return self.node_dist
   
    def print_node_dist(self):
        for key in self.node_dist.keys():
            print("node", key, ": ", self.node_dist[key])
        print("end node dist \n") 

#---------------------node_dist-----------------------------------------

# Source: https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/representing-graphs-in-code/


#------------------creating graph ---------------------------------
class BuildGraph:

    def __init__(self, file, file2):
        self.file = file
        self.file2 = file2
        


    def build_graph(self):
            # row count other than first line of headers is number of stations
        with open('_dataset/london.stations.csv') as self.file:
            stations = csv.reader(self.file)
            numStations = sum(1 for row in stations)+1

            graph = Graph(numStations)

            #Have to open it again for some reason
            with open('_dataset/london.stations.csv') as self.file:
                stations = csv.reader(self.file)
                for fileLine in stations:
                    if stations.line_num != 1:
                        graph.add_node_dist(float(fileLine[0]), float(fileLine[1]), float(fileLine[2]))
            with open('_dataset/london.connections.csv') as self.file2:
                connections = csv.reader(self.file2)
                for fileLine in connections:
                    #print(fileLine)
                    if connections.line_num != 1:
                        graph.add_edge(int(fileLine[0]), int(fileLine[1]), int(fileLine[3]))
            return graph
                    
   #------------------creating graph ---------------------------------     
with open('_dataset/london.stations.csv') as file:
            stations = csv.reader(file)

with open('_dataset/london.connections.csv') as file2:
                connections = csv.reader(file2)

# app = BuildGraph(file,file2)
# graph = app.build_graph()
# graph.print_adj_list()
# graph.print_node_dist()

