from matplotlib import pyplot as plt
from abc import ABC, abstractmethod
from BuildGraph import BuildGraph
#


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
class graphMetricsStrategy(ABC):
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


      #account for duplicates
class numEdgesStrategy(graphMetricsStrategy):
   def create_metric(self, m_adj_list):
      edges = 0
      for node in m_adj_list:
         for tuple in m_adj_list[node]:
               edges += 1
      return edges

app = BuildGraph()
graph = app.build_graph()

adjList = graph.get_adjList()

def process_metrics(processingStrategy: graphMetricsStrategy):
   metric = processingStrategy.create_metric(adjList)
   return metric
 #--------------- STRATEGY PATTERN ------------------------------------------------------  


  
# ------------------------------------------- Run metrics (maybe put this is test) --------------------->
#process_metrics(numEdgesStrategy()) 
degrees = process_metrics(nodeDegreeStrategy())


#degree    
dev_x = []
#number of nodes with such degree
dev_y = []

index = 0

def graph_degree(metric):
   #iterate through each (node,degree) tuple from metric
   for tuple in metric:
      #skip first entry
      if(tuple[0] == 0):
         continue
      elif(tuple[0] == 1):
         dev_x.append(tuple[1])
         dev_y.append(1)
         continue
      #check if the degree is in x axis
      if tuple[1] in dev_x:
         #increment corresponding y index
         index = dev_x.index(tuple[1])
         dev_y[index] = dev_y[index] + 1
      #create new index for x and y axis    
      else:
         #insert degree in x in ascending order, and create an index for corresponding y as well

         for i in reversed(dev_x):
            check = False
            if tuple[1] > i:
               index = dev_x.index(i)    
               dev_x.insert(index+ 1,tuple[1])
               dev_y.insert(index +1, 1)
               check = True
               break
         #if check is never switched to true, tuple is smaller than everything so insert at beginning
         if check == False:
            dev_x.insert(0,tuple[1])
            dev_y.insert(0, 1)
         
   print(dev_x , "dev_x")
   print(dev_y , "dev_y")
   return dev_x,dev_y
#deg = [(0,0), (1,4), (2,4), (3,3),(4,2),(5,5),(6,7),(7,6),(8,1),(9,7),(10,6) ]
devX,devY = graph_degree(degrees)

# plot graph ------------->
# plt.plot(devX, devY)

# plt.xlabel('degree')
# plt.ylabel('# of nodes')
# plt.title('distribution of nodes degree')



















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