
from Algorithms.AlgorithmsStrategy import GraphAlgoInterface
#from Metrics.MetricsStrategy import *
from Graphing.Graph import *

import random

class BenchmarkSpace:

    graph = list 
    graphs = list[graph]

    def seperateCounts(self, countList):
        aCount = []
        bCount = []

        for count in range(len(countList)):
            if count % 2 == 1:
                aCount.append(countList[count])
            if count %2 == 0:
                bCount.append(countList[count])
        return aCount,bCount

 
# -------------------GENERATE RANDOM GRAPH--------------------------------------        
    def withNbStations(self,stationsList):
        #for each test number of nodes, create a graph with that amount of nodes and randomly create each edge/location
        graphs = []
        for numNodes in stationsList:
            print("made graph" , numNodes)
            graph = Graph(numNodes+1)
            for i in range(1,numNodes+1):
                #print(graph.print_adj_list())
                if(i == 0):
                    continue
                graph.add_node_loc(i,  random.uniform(-0.7,0.7), random.uniform(51,52))
                graph.add_edge(i, random.randint(1,numNodes),random.randint(1,3), random.randint(1,13))
            graphs.append(graph)
        return graphs





# --------------------- Benchmark Algorithms -------------------------
    def withOpsAlgoStrategies(self, graphs, algoOpStrategy: GraphAlgoInterface,start, end):
        #for each test graph run both algorithms
        allCounts = []
        for graph in graphs:
            print("----------------------paths--------------------")
            for algo in algoOpStrategy:
                count = algo.execute(graph, start, end)
                allCounts.append(count)
        dCount, aCount = self.seperateCounts(allCounts)

        return dCount, aCount



    def withTimeAlgoStrategies(self, graphs, algoTimeStrategy: GraphAlgoInterface,start, end):
    #for each test graph run both algorithms
        times = []
        for graph in graphs:
            print("----------------------paths--------------------")
            for algo in algoTimeStrategy:
                time = algo.execute(graph, start, end)
                times.append(time)
        dtime, atime = self.seperateCounts(times)
                

        return dtime, atime 

# --------------------- Benchmark Metrics -------------------------





    
        
        

        


