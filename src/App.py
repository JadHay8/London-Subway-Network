from Graphing.BuildGraph import BuildGraph
from Algorithms.AlgorithmsStrategy import *
from Metrics.MetricsStrategy import *
from BenchmarkSpace import *
from matplotlib import pyplot as plt
import pyperf
from Algorithms.HamiltonCycle import Hamiltonian


from Plotting.DegreePlot import DegreePlot
#from Test import *


class App:
    
    def main():

        app = BuildGraph()
        graph = app.build_graph()
        adjList = graph.get_adjList()
        start = 1
        stop = 10



        #------------- CALLING STRATEGIES -----------------------------------------------
        def process_metrics(processingStrategy: graphMetricsInterface):
            metric = processingStrategy.create_metric(adjList)
            return metric
        def process_graph(processingStrategy: GraphAlgoInterface):
            shortestPath = processingStrategy.execute(graph, start, stop)
            return shortestPath
        #------------- CALLING STRATEGIES -----------------------------------------------




    # ------------------Running BenchmarkSpace---------------
        algorithms = [AStarStrategy(), dijkstraStrategy()]
        metrics = [nodeDegreeStrategy(),numEdgesStrategy()]
        space = BenchmarkSpace()
        graphs = space.withNbStations([10,50,100,250])

        # -------------- algo Ops benchmark ---------------
        #dCount, aCount = space.withOpsAlgoStrategies(graphs, algorithms, 1, 10)
        #print (dCount, aCount)

        # -------------- algo Time benchmark ---------------

        dtime, atime = space.withTimeAlgoStrategies(graphs, algorithms, 1, 10)
        print (dtime, atime)


        # -------------- metric benchmark --------------------
        # dCount, eCount = space.withMetricStrategies(graphs,metrics)
        # print(dCount, eCount)
            

    #--------------- PLOTTING Algo BENCHMARK---------
        def plot_algoOps(dCount,aCount):
            fig,axes = plt.subplots()
            scope = [10, 50, 100, 250]
            axes.set(xlabel = 'Graph size', ylabel = 'Operations')
            axes.plot(scope, [y for y in dCount] [:len(scope)], '-', label="Dijkstra")
            axes.plot(scope, [y for y in aCount] [:len(scope)], '-', label="AStar")
            axes.legend()
            fig.savefig('Outputs.Operations.pdf')
            plt.show()

        def plot_algoTime(dTime,aTime):
            fig,axes = plt.subplots()
            scope = [10, 50, 100, 250]
            axes.set(xlabel = 'Graph size', ylabel = 'Time (Milliseconds)')
            axes.plot(scope, [y for y in dTime] [:len(scope)], '-', label="Dijkstra")
            axes.plot(scope, [y for y in aTime] [:len(scope)], '-', label="AStar")
            axes.legend()
            fig.savefig('Outputs.Time.pdf')
            plt.show()

        #--------------- PLOTTING Metrics BENCHMARK---------


        #plot_algoOps(dCount,aCount)
        plot_algoTime(dtime,atime)

        

        



        # ----------------RUNNING METRICS--------------
        # test = process_metrics(numEdgesStrategy())
        # print(test)


        # ------------------ PLOTTING METRIC (NODE DEGREES) -----------------
        # plot = DegreePlot()
        # degrees = process_metrics(nodeDegreeStrategy())
        # plot.graph_degree_plot(degrees)




        # ----------- PRINTING GRAPH -------------------------------
        # graph.print_adj_list()
        # graph.print_node_loc()
        # print(graph.get_node_loc(7))







        #--------------------- TESTING ALGORITHMS ------------------------
        # app = BuildGraph()
        # graph = app.build_graph()
        # start = 1
        # stop = 10
        # print("A STAR ---------------------------------------------")
        # # needed to add a second variable to fit strategy pattern
        # shortest_path = process_graph(AStarStrategy())

        # print("Dijkstra ---------------------------------------------")
        # shortest_path = process_graph(dijkstraStrategy())
        # print(shortest_path)


        

        
    main()

       





        # # ------------------Running Benchmark---------------   
        # space = BenchmarkSpace(1,10)
        # the_graphs = space.withNbStations([10,50,100, 250])
        # algorithms = [AStarStrategy(), dijkstraStrategy()]

        # def do_Bench(processingStrategy: GraphAlgoInterface, graphs):
        #     runner = pyperf.Runner()
        #     # Baseline run
        #     for graph in graphs:
        #         print("----------------------paths--------------------")
        #         for algo in processingStrategy:
        #                 runner.bench_func(algo.execute(graph, 1, 10), graph )
        #                 print("done")
            
        # do_Bench(algorithms, the_graphs)
         