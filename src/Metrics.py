from abc import ABC, abstractmethod
from Graph import Graph
from Graph import BuildGraph
import csv
import math


#GRAPH (ADJ_LST) TEST CODE-------->
# graph = Graph(10)
# graph.add_edge(1, 2, 3)
# graph.add_edge(5, 3, 2)
# graph.add_edge(8, 4, 6)
# graph.add_edge(4, 8, 6)
# graph.add_edge(8, 7, 2)
# graph.add_edge(9, 7, 1)
# graph.add_edge(9, 8, 3)
# graph.add_edge(6, 0, 2)


#GRAPH (NODE_DIST) TEST CODE ---------------->
# graph = Graph(5)
# graph.add_node_dist(1, 51.5846, -0.2786)
# graph.add_node_dist(2, 51.4991, -0.1115)
# graph.add_node_dist(3, 51.5119, -0.1756)



with open('_dataset/london.stations.csv') as file:
            stations = csv.reader(file)

with open('_dataset/london.connections.csv') as file2:
                connections = csv.reader(file2)
app = BuildGraph(file,file2)
graph = app.build_graph()

adjList = graph.get_adjList()
nodeDist = graph.get_node_dist()

#--------------- STRATEGY PATTERN ------------------------------------------------------
#abstract method
class graphMetricsStrategy(ABC,Graph):
   @abstractmethod
   #call with adj_list from graph
   def create_metric(self, m_adj_list): #add -> to specify return type 
     pass

class nodeDegreeStrategy(graphMetricsStrategy):
   def create_metric(self, m_adj_list):
      degOfNodes = []
      #iterate through each node in the list
      for node in m_adj_list:
         degree = 0
         duplicate = []
         #check if the connection has already been accounted for (would add a duplicate), otherwise increment degree
         for tuple in m_adj_list[node]:
            if tuple[0] in duplicate:
               continue
            duplicate.append(tuple[0])
            degree += 1
         degOfNodes.append((node,degree))
      return degOfNodes


class numEdgesStrategy(graphMetricsStrategy):
   def create_metric(self, m_adj_list):
      edges = 0
      for node in m_adj_list:
         for tuple in m_adj_list[node]:
               edges += 1
      return edges

# may not be able to use in strategy pattern -------------------------->

class nodeDistanceStrategy(graphMetricsStrategy):
   def create_metric(self, m_adj_list):
      return 9

   # implementation with nodeOne and nodeTwo
   # def create_metric(self, nodeOne, nodeTwo):
   #      node_dist = graph.get_node_dist()
   #      temp = node_dist[nodeOne]
   #      temp2 = node_dist[nodeTwo]

   #      #must be a better way
   #      for i in temp:
   #       nodeOneLong = i[0]
   #       nodeOneLat = i[1]
   #      for j in temp2:
   #       nodeTwoLong = j[0]
   #       nodeTwoLat = j[1]

   #      a = nodeOneLong - nodeTwoLong
   #      b = nodeOneLat - nodeTwoLat
   #      c = math.sqrt(a**2 + b**2)
   #      return c

         
      

def process_metrics(processingStrategy: graphMetricsStrategy):
   metric = processingStrategy.create_metric(adjList)
   print(metric) 

  
# Run metrics --------->
#process_metrics(numEdgesStrategy(1))    #figure out why we need a random parameter
#process_metrics(nodeDistanceStrategy(1))
#process_metrics(nodeDegreeStrategy(1))



#--------------- STRATEGY PATTERN ------------------------------------------------------
















# -------------------ONE NODE TO EVERY NODE IMPLEMENTATION NODE DISTANCE ---------------------------------------
# def nodeDistance(node_dist,nodeLong, nodeLat):
#    distances = []
#    for node in node_dist:
#       for tuple in node_dist[node]:
#          #print(tuple)
#          if(tuple[0] == nodeLong and tuple[1] == nodeLat):
#             continue
#          else:
#             long = tuple[0]
#             lat = tuple[1]
#             a = nodeLong - long
#             b = nodeLat - lat
#             c = math.sqrt(a**2 + b**2)
#          distances.append((node, c))
#          print(node, c)
#     return distances
# nodeDistance(nodeDist, 51.4991, -0.1115)
# -------------------ONE NODE TO EVERY NODE IMPLEMENTATION NODE DISTANCE ---------------------------------------    


#------------------creating graph ---------------------------------
# with open('_dataset/london.stations.csv') as file:
#     stations = csv.reader(file)

#     # row count other than first line of headers is number of stations
#     numStations = sum(1 for row in stations)+1

#     graph = Graph(numStations)

#     #Have to open it again for some reason
#     with open('_dataset/london.stations.csv') as filee:
#         stationss = csv.reader(filee)
#         for fileLine in stationss:
#             if stationss.line_num != 1:
#                 graph.add_node_dist(float(fileLine[0]), float(fileLine[1]), float(fileLine[2]))

#     with open('_dataset/london.connections.csv') as file2:
#         connections = csv.reader(file2)
#         for fileLine in connections:
#             #print(fileLine)
#             if connections.line_num != 1:
#                 graph.add_edge(int(fileLine[0]), int(fileLine[1]), int(fileLine[3]))
#------------------creating graph ---------------------------------