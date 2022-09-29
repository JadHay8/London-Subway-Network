from Graphing.BuildGraph import BuildGraph
from Algorithms.AlgorithmsStrategy import *
from Metrics.MetricsStrategy import *
from BenchmarkSpace import *

from Plotting.DegreePlot import DegreePlot
from Test import *


class App:
    
    def main():
        def process_metrics(processingStrategy: graphMetricsInterface):
            metric = processingStrategy.create_metric(adjList)
            return metric
        def process_graph(processingStrategy: GraphAlgoInterface):
            shortestPath = processingStrategy.execute(graph, start, stop)
            return shortestPath
                    
        
        
        
        
        
        app = BuildGraph()
        graph = app.build_graph()
        adjList = graph.get_adjList()
        
        # ----------------running metrics--------------
        test = process_metrics(numEdgesStrategy())
        print(test)

        
        #-------------running test ------------
        





        # ------------------Running Benchmark---------------

        #figure out how to make start and stop variable
        start = 1
        stop = 286
        space = BenchmarkSpace(1,10)
        the_graphs = space.withNbStations([10,50,100])
        algorithms = [AStarStrategy(), dijkstraStrategy()]
        dCount, aCount = space.withStrategies(the_graphs, algorithms)
        print (dCount, aCount)
        # # space.do_Bench(algorithms, the_graphs)


        #algorithms = [AStarStrategy(), dijkstraStrategy()]
       




        # print("A STAR ---------------------------------------------")
        # # needed to add a second variable to fit strategy pattern
        #shortest_path = process_graph(AStarStrategy())

        # print("Dijkstra ---------------------------------------------")
        # shortest_path = process_graph(dijkstraStrategy())
        # print(shortest_path)
        # # dijkstra_print_result(previous_nodes, shortest_path, 1, 286)


        
        # ------------------plot graph-----------------
        #uncomment stuff to plot graph.. I had to bc I still have error
        # plot = DegreePlot()
        # degrees = process_metrics(nodeDegreeStrategy())
        # plot.graph_degree_plot(degrees)

        
        

        #test graph ---->>
        # graph.print_adj_list()
        # graph.print_node_loc()
        # print(graph.get_node_loc(7))


        

        
    main()

       
