from abstractMetrics import graphMetricsStrategy

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