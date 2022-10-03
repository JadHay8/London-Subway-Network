from Graphing.BuildGraph import BuildGraph
from Metrics.MetricsStrategy import *
from Algorithms.AlgorithmsStrategy import *
from KPIBenches.opsBench import AStarOps, DijkstraOps
from KPIBenches.timeBench import AStarTime, DijkstraTime
from BenchmarkSpace import *

from Plotting.DegreePlot import DegreePlot
from Plotting.OpsPlot import OpsPlot
from Plotting.TimePlot import TimePlot

from Algorithms.HamiltonCycle import HamiltonCycle

#from Test import *


class App:

    def main():

        app = BuildGraph()
        graph = app.build_graph()
        adjList = graph.get_adjList()
        start = 1
        stop = 10

        # ------------- CALLING STRATEGIES -----------------------------------------------

        def process_metrics(processingStrategy: graphMetricsInterface):
            metric = processingStrategy.create_metric(adjList)
            return metric

        def process_graph(processingStrategy: GraphAlgoInterface):
            shortestPath = processingStrategy.execute(graph, start, stop)
            return shortestPath
        #------------- CALLING STRATEGIES -----------------------------------------------




    # ------------------Running BenchmarkSpace---------------
        algorithms = [AStarStrategy(), DijkstraStrategy()]
        algorithmsOps = [AStarOps(), DijkstraOps()]
        algorithmsTime = [AStarTime(),DijkstraTime()]
        space = BenchmarkSpace()
        graphs = space.withNbStations([10,50,100,250])

        # -------------- algo Ops benchmark ---------------
        # dCount, aCount = space.withOpsAlgoStrategies(graphs, algorithmsOps, 1, 10)
        # print (dCount, aCount)

        # -------------- algo Time benchmark ---------------
        # dtime, atime = space.withTimeAlgoStrategies(graphs, algorithmsTime, 1, 10)
        # print (dtime, atime)



        #--------------- PLOTTING Algo BENCHMARK---------
        # plot = OpsPlot()
        # plot.plot_algoOps(dCount, aCount)

        # plot = TimePlot()
        # plot.plot_algoTime(dtime, atime)


        

        # ----------------RUNNING METRICS--------------
        # test = process_metrics(numEdgesStrategy())
        # print(test)

        # ------------------ PLOTTING METRIC (NODE DEGREES) -----------------
        plot = DegreePlot()
        degrees = process_metrics(nodeDegreeStrategy())
        plot.graph_degree_plot(degrees)

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
        # print(shortest_path)

        # print("Dijkstra ---------------------------------------------")
        # shortest_path = process_graph(DijkstraStrategy())
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
         