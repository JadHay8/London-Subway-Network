from abc import ABC, abstractmethod
from graph import CreateGraph

#abstract method
class graphMetricsStrategy(ABC,CreateGraph):
    @abstractmethod
    #call with adj_list from graph
    def create_metric(self, m_adj_list): #add -> to specify return type 
      pass


class numEdgesStrategy(graphMetricsStrategy):
    def create_metric(self, m_adj_list):
      for i in m_adj_list:
        pass
      return 9

class avgNodeDegStrategy(graphMetricsStrategy):
    def create_metric(self, m_adj_list ):
      return m_adj_list#create calculation

def process_graph(self, processingStrategy: graphMetricsStrategy):
   print("hello")
   numEdges = processingStrategy.create_metric(CreateGraph.adjList)
   print(numEdges)

app = CreateGraph()

process_graph(numEdgesStrategy())


