from BuildGraph import BuildGraph
from Algorithms import *
from abstractMetrics import *
from DegreePlot import DegreePlot
#from matplotlib import pyplot as plt




class App:
    
    
    def main():
        def process_metrics(processingStrategy: graphMetricsInterface):
            metric = processingStrategy.create_metric(adjList)
            return metric
        def process_graph(processingStrategy: GraphAlgoInterface):
            shortestPath = processingStrategy.execute()
            return shortestPath
                    
        
        
        
        
        
        app = BuildGraph()
        graph = app.build_graph()
        adjList = graph.get_adjList()
        
        # ----------------running metrics--------------
        test = process_metrics(numEdgesStrategy())
        #print(test)

        

        # ------------------run algorithms---------------

        #figure out how to make start and stop variable
        start = 1
        stop = 286

        print("A STAR ---------------------------------------------")
        # needed to add a second variable to fit strategy pattern
        shortest_path = process_graph(AStarStrategy(graph, start, stop))

        print("Dijkstra ---------------------------------------------")
        shortest_path = process_graph(dijkstraStrategy(graph, start, stop))
        print(shortest_path)
        # dijkstra_print_result(previous_nodes, shortest_path, 1, 286)


        
        # ------------------plot graph-----------------
        #uncomment stuff to plot graph.. I had to bc I still have error
        plot = DegreePlot()
        degrees = process_metrics(nodeDegreeStrategy())
        plot.graph_degree_plot(degrees)

        
        

        #test graph ---->>
        # graph.print_adj_list()
        # graph.print_node_loc()
        # print(graph.get_node_loc(7))


        

        
    main()

       
