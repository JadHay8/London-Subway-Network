import csv
from abstractMetrics import *

from Graph import Graph
from BuildGraph import BuildGraph
from Algorithms import Algorithm


app = Algorithm()


def test():
    with open('_dataset/london.stations.csv') as file:
        stations = csv.reader(file)

        # row count other than first line of headers is number of stations
        numStations = sum(1 for row in stations)+1

        graph = Graph(numStations)

        with open('_dataset/london.connections.csv') as file2:
            connections = csv.reader(file2)
            for fileLine in connections:
                if connections.line_num != 1:
                    graph.add_edge(int(fileLine[0]), int(
                        fileLine[1]), int(fileLine[3]))

    # graph.print_adj_list()

    # graph = Graph(10)
    # graph.add_edge(1, 2, 3)
    # graph.add_edge(5, 3, 2)
    # graph.add_edge(8, 4, 6)
    # graph.add_edge(8, 7, 2)
    # graph.add_edge(9, 7, 1)
    # graph.add_edge(9, 8, 3)
    # graph.add_edge(6, 0, 2)

    # graph.print_adj_list()

    previous_nodes, shortest_path = app.dijkstra(graph, 1)

    app.dijkstra_print_result(previous_nodes, shortest_path, 1, 286)

# test()


def test_a_star():
    # graph = Graph(10)
    # graph.add_edge(1, 2, 3)
    # graph.add_edge(5, 3, 2)
    # graph.add_edge(8, 4, 6)
    # graph.add_edge(8, 7, 2)
    # graph.add_edge(9, 7, 1)
    # graph.add_edge(9, 8, 3)
    # graph.add_edge(6, 0, 2)

    with open('_dataset/london.stations.csv') as file:
        stations = csv.reader(file)

        graph = Graph(1+sum(1 for row in stations))

        # Go back to beginning of file by reopening

        with open('_dataset/london.stations.csv') as filee:
            stationss = csv.reader(filee)
            for fileLine in stationss:
                if stationss.line_num != 1:
                    graph.add_node_loc(float(fileLine[0]), float(
                        fileLine[1]), float(fileLine[2]))

        with open('_dataset/london.connections.csv') as file2:
            connections = csv.reader(file2)
            for fileLine in connections:
                # print(fileLine)
                if connections.line_num != 1:
                    graph.add_edge(int(fileLine[0]), int(
                        fileLine[1]), int(fileLine[3]))

# app2 = BuildGraph()
# graph = app2.build_graph()
#app.a_star_algorithm(graph, 1, 286)


app = BuildGraph()
graph = app.build_graph()

adjList = graph.get_adjList()


def process_metrics(processingStrategy: graphMetricsStrategy):
    metric = processingStrategy.create_metric(adjList)
    print(metric)


# Run metrics --------->
# process_metrics(numEdgesStrategy(1))    #figure out why we need a random parameter
process_metrics(nodeDegreeStrategy(1))
