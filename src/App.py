from Graphing.BuildGraph import BuildGraph
from Algorithms.AlgorithmsStrategy import *
from Metrics.MetricsStrategy import *
from BenchmarkSpace import *
from matplotlib import pyplot as plt


from Plotting.DegreePlot import DegreePlot
from Test import *


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
                    
        
        

        
        

        

         # ------------------Running Benchmark---------------

        #figure out how to make start and stop variable
        # start = 1
        # stop = 286
        # space = BenchmarkSpace(1,10)
        # the_graphs = space.withNbStations([10,50,100])
        # algorithms = [AStarStrategy(), dijkstraStrategy()]
        # dCount, aCount = space.withStrategies(the_graphs, algorithms)
        # print (dCount, aCount)
        # # space.do_Bench(algorithms, the_graphs)


        #algorithms = [AStarStrategy(), dijkstraStrategy()]




        #--------------- PLOTTING BENCHMARK---------
        space = BenchmarkSpace(1,10)
        graphs = space.withNbStations([10,50,100, 250])
        dCount, aCount = space.withStrategies(graphs, [AStarStrategy(), dijkstraStrategy()])

        print (dCount, aCount)

        fig,axes = plt.subplots()
        scope = [10, 50, 100, 250]
        axes.set(xlabel = 'Graph size', ylabel = 'comparisons')
        axes.plot(scope, [y for y in dCount] [:len(scope)], '-', label="Dijkstra")
        axes.plot(scope, [y for y in aCount] [:len(scope)], '-', label="AStar")
        axes.legend()
        fig.savefig('Outputs.Comparisons.pdf')
        plt.show()



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

        # print("A STAR ---------------------------------------------")
        # # needed to add a second variable to fit strategy pattern
        #shortest_path = process_graph(AStarStrategy())

        # print("Dijkstra ---------------------------------------------")
        # shortest_path = process_graph(dijkstraStrategy())
        # print(shortest_path)
        # # dijkstra_print_result(previous_nodes, shortest_path, 1, 286)

        

        
    main()

       
