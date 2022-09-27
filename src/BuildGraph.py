from Graph import Graph
import csv

class BuildGraph:   

    def build_graph(self):
            # row count other than first line of headers is number of stations
        with open('_dataset/london.stations.csv') as self.file:
            stations = csv.reader(self.file)
            numStations = sum(1 for row in stations)+1

            graph = Graph(numStations)

            #Have to open it again for some reason
            with open('_dataset/london.stations.csv') as self.file:
                stations = csv.reader(self.file)
                for fileLine in stations:
                    if stations.line_num != 1:
                        graph.add_node_loc(float(fileLine[0]), float(fileLine[1]), float(fileLine[2]))
            with open('_dataset/london.connections.csv') as self.file2:
                connections = csv.reader(self.file2)
                for fileLine in connections:
                    #print(fileLine)
                    if connections.line_num != 1:
                        #station1, station2, weight, line
                        graph.add_edge(int(fileLine[0]), int(fileLine[1]),int(fileLine[3]), int(fileLine[2]))
            return graph
                
   #------------------creating graph ---------------------------------     
