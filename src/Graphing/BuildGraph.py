from .Graph import Graph
import csv


class BuildGraph:
    graph = list[dict]

    def build_graph(self) -> graph:
        # row count other than first line of headers is number of stations
        with open('_dataset/london.stations.csv') as self.file:
            stations = csv.reader(self.file)
            numStations = sum(1 for row in stations)+1

            graph = Graph(numStations)

            # Have to open it again for some reason
            with open('_dataset/london.stations.csv') as self.file:
                stations = csv.reader(self.file)
                for fileLine in stations:
                    if stations.line_num != 1:
                        graph.add_node_loc(int(fileLine[0]), float(
                            fileLine[1]), float(fileLine[2]))
            with open('_dataset/london.connections.csv') as self.file2:
                connections = csv.reader(self.file2)
                for fileLine in connections:
                    # print(fileLine)
                    if connections.line_num != 1:
                        #station1, station2, weight, line
                        graph.add_edge(int(fileLine[0]), int(
                            fileLine[1]), int(fileLine[3]), int(fileLine[2]))
                        # add node, line to {node: lines} dictionary for actual data storage
                        graph.add_node_line(int(fileLine[0]), int(fileLine[2]))
            return graph

    def get_nodes(self) -> int:
        with open('_dataset/london.stations.csv') as file:
            stations = csv.reader(file)
            print(sum(1 for row in stations)+1)
            return sum(1 for row in stations)+1

    def get_num_edes(self) -> int:
        with open('_dataset/london.connections.csv') as file:
            connections = csv.reader(file)
            return sum(1 for fileLine in connections) - 1 #exclude header

    # def get_edges(self):
    #     g = BuildGraph().build_graph()
    #     adj_list = g.get_adjList()

    #     for node in adj_list:
    #         #somehow return all edge pairs?







   # ------------------creating graph ---------------------------------
