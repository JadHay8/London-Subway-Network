
from Algorithms.AlgorithmsStrategy import *
from Graphing.Graph import *
import pyperf
import random

class BenchmarkSpace:
    def __init__(self, start, end):
        self.start = start
        self.end = end
 
        


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

    def withStrategies(self, graphs, processingStrategyOne: GraphAlgoInterface):
        #for each test graph run both algorithms
        allCounts = []
        for graph in graphs:
            print("----------------------paths--------------------")
            for algo in processingStrategyOne:
                path , count = algo.execute(graph, self.start, self.end)
                print(path)
                allCounts.append(count)
        dCount = []
        aCount = []

        for count in range(len(allCounts)):
            if count % 2 == 1:
                dCount.append(allCounts[count])
            if count %2 == 0:
                aCount.append(allCounts[count])
            

        return dCount, aCount

    # def do_Bench(self, processingStrategyOne: GraphAlgoInterface, graphs: list[int]):
    #     runner = pyperf.Runner()
    #     # Baseline run
    #     for graph in graphs:
    #         print("----------------------paths--------------------")
    #         for algo in processingStrategyOne:
    #                 runner.bench_func("dijkstra",  algo.execute(graph, self.start, self.end) , graphs)
    #                 runner.bench_func("AStar",algo.execute(graph, self.start, self.end), graphs )
    #                 print("done")





        


