from abc import ABC, abstractmethod


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
class graphMetricsInterface(ABC):
   opsCounter = 0
   def _ops(self):
      self.opsCounter  += 1
   def get_ops(self):
      return self.opsCounter

   @abstractmethod
   #call with adj_list from graph
   def create_metric(self, m_adj_list): #add -> to specify return type 
     pass

class nodeDegreeStrategy(graphMetricsInterface):
   def create_metric(self, m_adj_list):
      degOfNodes = []
      #iterate through each node in the list
      for node in m_adj_list:
         super()._ops()
         degree = 0
         duplicate = []
         #check if the connection has already been accounted for (would add a duplicate), otherwise increment degree
         for tuple in m_adj_list[node]:
            super()._ops()
            if tuple[0] in duplicate:
               super()._ops()
               continue
            duplicate.append(tuple[0])
            super()._ops()
            degree += 1
         degOfNodes.append((node,degree))
         super()._ops()
      ops = super().get_ops()
      return degOfNodes, ops


      #account for duplicates
class numEdgesStrategy(graphMetricsInterface):
   def create_metric(self, m_adj_list):
      edges = 0
      for node in m_adj_list:
         super()._ops()
         for tuple in m_adj_list[node]:
            super()._ops()
            edges += 1
      ops = super().get_ops()
      #account for duplicate edges(undirected)
      edges = edges/2
      return edges, ops

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
