
from Algorithms.AlgorithmsStrategy import *
from Metrics.MetricsStrategy import *
from Graphing.Graph import *

import random

class BenchmarkSpace:
    # def __init__(self, start, end):
    #     self.start = start
    #     self.end = end

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
    def withOpsAlgoStrategies(self, graphs, algoStrategy: GraphAlgoInterface,start, end):
        #for each test graph run both algorithms
        allCounts = []
        for graph in graphs:
            print("----------------------paths--------------------")
            for algo in algoStrategy:
                path , count, time = algo.execute(graph, start, end)
                print(path)
                allCounts.append(count)
        dCount, aCount = self.seperateCounts(allCounts)

            

        return dCount, aCount



    def withTimeAlgoStrategies(self, graphs, algoStrategy: GraphAlgoInterface,start, end):
    #for each test graph run both algorithms
        times = []
        for graph in graphs:
            print("----------------------paths--------------------")
            for algo in algoStrategy:
                path , count, time = algo.execute(graph, start, end)
                print(path)
                times.append(time)
        dtime, atime = self.seperateCounts(times)
                

        return dtime, atime 














        

# --------------------- Benchmark Metrics -------------------------

    def withMetricStrategies(self, graphs,metricStrategy: graphMetricsInterface):
        adj_lists = []
        values = []
        allOps = []
        for graph in graphs:
            adjList = graph.get_adjList()
            adj_lists.append(adjList)

        for list in adj_lists:
            for metric in metricStrategy:
                value, op = metric.create_metric(list)
                allOps.append(op)
                values.append(value)
        dCount, eCount = self.seperateCounts(allOps)

        return dCount, eCount




    
        
        

        


