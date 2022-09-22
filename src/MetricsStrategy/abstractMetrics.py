from abc import ABC, abstractmethod
from Graph import Graph
import csv
from nodeDegree import nodeDegreeStrategy



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






#--------------- STRATEGY PATTERN ------------------------------------------------------
#abstract method
class graphMetricsStrategy(ABC,Graph):
   @abstractmethod
   #call with adj_list from graph
   def create_metric(self, m_adj_list): #add -> to specify return type 
     pass



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