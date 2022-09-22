from abstractMetrics import graphMetricsStrategy

#account for duplicates
class numEdgesStrategy(graphMetricsStrategy):
   def create_metric(self, m_adj_list):
      edges = 0
      for node in m_adj_list:
         for tuple in m_adj_list[node]:
               edges += 1
      return edges