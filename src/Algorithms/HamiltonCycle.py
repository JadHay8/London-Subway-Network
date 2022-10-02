import csv
import sys
import os
 
# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
 
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
 
# adding the parent directory to
# the sys.path.
sys.path.append(parent)


from Graphing.Graph import *
from Graphing.BuildGraph import *



# class Hamiltonian:
#     def __init__(self, start, graph):
#         # start (& end) vertex
#         self.start = start
#         self.graph = graph

#         # list to store the cycle path
#         self.cycle = []

#         # varibale to mark if graph has the cycle
#         self.hasCycle = False

#     # method to inititate the search of cycle
#     def findCycle(self):
#         # add starting vertex to the list
#         self.cycle.append(self.start)

#         # start the search of the hamiltonian cycle
#         self.solve(self.start)

#     # recursive function to implement backtracking
#     def solve(self, vertex):
#         # Base condition: if the vertex is the start vertex
#         # and all nodes have been visited (start vertex twice)
#         if vertex == self.start and len(self.cycle) == N+1:
#             self.hasCycle = True

#             # output the cycle
#             self.displayCycle()

#             # return to explore more cycles
#             return

#         # iterate through the neighbor vertices
#         for i in range(len(vertices)):
#             adjList = self.graph.get_adjList()
#             if adjList[vertex][i] == 1 and visited[i] == 0:
#                 nbr = i
#                 # visit and add vertex to the cycle
#                 visited[nbr] = 1
#                 self.cycle.append(nbr)

#                 # traverse the neighbor vertex to find the cycle
#                 self.solve(nbr)

#                 # Backtrack
#                 visited[nbr] = 0
#                 self.cycle.pop()

#     # function to display the hamiltonian class
#     def displayCycle(self):
#         names = []
#         for v in self.cycle:
#             names.append(vertices[v])
#         print(names)


# if __name__ == '__main__':
#     vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
#     adjacencyM = [[0, 1, 0, 0, 0, 0, 0, 1],
#                   [1, 0, 1, 0, 0, 0, 0, 0],
#                   [0, 1, 0, 1, 0, 0, 0, 1],
#                   [0, 0, 1, 0, 1, 0, 1, 0],
#                   [0, 0, 0, 1, 0, 1, 0, 0],
#                   [0, 0, 0, 0, 1, 0, 1, 0],
#                   [0, 0, 0, 1, 0, 1, 0, 1],
#                   [1, 0, 1, 0, 0, 0, 1, 0]]
#     # list mapping of vertices to mark vertex visited
#     visited = [0 for x in range(len(vertices))]

#     # number of vertices in the graph
#     N = 8

#     # Driver code
#     hamiltonian = Hamiltonian(0, adjacencyM)
#     hamiltonian.findCycle()

#     # if the graph doesn't have any Hamiltonian Cycle
#     if not hamiltonian.hasCycle:
#         print("No Hamiltonian Cycle")

#         # Site used: https://pencilprogrammer.com/algorithms/hamiltonian-cycle-using-backtracking/


class HamiltonCycle:
    # source: https://www.codespeedy.com/check-if-hamiltonian-cycle-exists-in-a-graph-using-python/

    def __init__(self, graph, start):
        self.graph = graph
        self.start = start
        self.path = []

        # ------------------------------------------

    '''
  Defining our safe vertex as
  something which is not in our
  path
  '''

    def safeVertex(self, node):
        if(node in self.path):
            return False

        return True
    # -------------------------------------------
    # -------------------------------------------
    '''
  Defining our DFS and 
  Backtracking Logic
  '''

    def cycleDetection(self, E, n, root):
        self.path.append(root)
        # Seeing all the neigbours of the current root
        for i in E[root]:
            # Checking if our vertex satisfies the safe Vertex
            if(self.safeVertex(i)):
                # Checking if a cycle has already been detected or not in the
                # ---------------------previous recursion--------------------
                if(self.cycleDetection(E, n, i)):
                    return True

        # Checking if our current self.path has all the vertices
        if(len(self.path) == n):
            # If there is an edge from last vertex to the first vertex in our self.path
            # -------------then we have an hamiltonian cycle---------------------
            if(self.path[0] in E[self.path[len(self.path)-1]]):
                return True
            else:
                return False
        # once we are done we remove that particle from the iteration
        self.path.pop()
    # -------------------------------------------
    # -------------------------------------------
    '''
  Printing True or False
  based on our output from Cycle Detection
  '''

    def HamiltonianCycle(self, E, n, root):
        if(self.cycleDetection(E, n, root)):
            print("True")
        else:
            print("False")

    # -------------------------------------------

    def build_hamilton_graph(self):
        bg = BuildGraph()
        graph = bg.build_graph()
        N_Vertices = bg.get_nodes()
        N_Edges = bg.get_num_edes()
        al = graph.get_adjList()
        edge_vertices = {node for node in al.keys()}

        i=0
        for (node,n) in zip(al.keys(),al.values()):
            l = []
            for tuple in n:
                l.append(tuple[0])

            edge_vertices[node] = l #-> {node: [node,node,...]}
            i += 1

        matrix = list()

        for i in range(N_Vertices):
            matrix.append([])

        # for j in range(N_Edges):
        #     # edge_vertices = input().split()
            
        #     u = int(edge_vertices[0])
        #     v = int(edge_vertices[1])
        #     matrix[u-1].append(v-1)
        #     matrix[v-1].append(u-1)

        for u in edge_vertices:
            for v in edge_vertices[node]:
                #TODO
                matrix[u-1].append(v-1)
                matrix[v-1].append(u-1)

        self.HamiltonianCycle(matrix, N_Vertices, 0)
        # This path is actually a Hamiltonian cycle.
        print(self.path)

        with open('_dataset/london.stations.csv') as self.file:
            stations = csv.reader(self.file)
            numStations = sum(1 for row in stations)+1

            graph = Graph(numStations)

            # Have to open it again for some reason
            with open('_dataset/london.stations.csv') as self.file:
                stations = csv.reader(self.file)
                for fileLine in stations:
                    if stations.line_num != 1:
                        graph.add_node_loc(int(fileLine[0]), float(
                            fileLine[1]), float(fileLine[2]))
            with open('_dataset/london.connections.csv') as self.file2:
                connections = csv.reader(self.file2)
                for fileLine in connections:
                    # print(fileLine)
                    if connections.line_num != 1:
                        #station1, station2, weight, line
                        graph.add_edge(int(fileLine[0]), int(
                            fileLine[1]), int(fileLine[3]), int(fileLine[2]))
                        # add node, line to {node: lines} dictionary for actual data storage
                        graph.add_node_line(int(fileLine[0]), int(fileLine[2]))
            return graph
