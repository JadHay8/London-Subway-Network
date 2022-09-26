from BuildGraph import BuildGraph
from abstractMetrics import graphMetricsInterface
from Algorithms import GraphAlgoInterface
from Algorithms import dijkstraStrategy
from Algorithms import AStarStrategy
from abstractMetrics import numEdgesStrategy
from abstractMetrics import nodeDegreeStrategy
from DegreePlot import DegreePlot




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

        plot = DegreePlot()
        

        degrees = process_metrics(nodeDegreeStrategy())
        devX,devY = plot.graph_degree_plot(degrees)
        print(devX, devY)

        test = process_metrics(numEdgesStrategy())
        print(test)

        start = 1  # how do we figure out what we start at
        stop = 286

        print("A STAR ---------------------------------------------")
        # needed to add a second variable to fit strategy pattern
        shortest_path = process_graph(AStarStrategy(graph, start, stop))

        print("Dijkstra ---------------------------------------------")
        shortest_path = process_graph(dijkstraStrategy(graph, start, stop))
        print(shortest_path)
        # dijkstra_print_result(previous_nodes, shortest_path, 1, 286)

    main()

       
