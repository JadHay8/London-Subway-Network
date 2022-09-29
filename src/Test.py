from Graphing.Graph import *
from Algorithms.AlgorithmsStrategy import *
import pytest
import random


    #figure out the return type of graph

    # @pytest.fixture
    # def empty_graph() -> dict():
    #     graph = Graph(0)
    #     return (graph, 0, 0)

@pytest.fixture
def one_node() -> dict():
    graph = Graph(1)
    graph.add_node_loc(1,  random.uniform(-0.7,0.7), random.uniform(51,52))
    graph.add_edge(1, 1 ,random.randint(1,3), random.randint(1,13))
    return (graph,1,1)

@pytest.fixture
def random_graph() -> dict():
    numNodes = random.randint(1,50)
    graph = Graph(numNodes)
    for i in range(1,numNodes+1):
        #print(graph.print_adj_list())
        if(i == 0):
            continue
        graph.add_node_loc(i,  random.uniform(-0.7,0.7), random.uniform(51,52))
        graph.add_edge(i, random.randint(1,numNodes),random.randint(1,3), random.randint(1,13))
    return (graph, 1, numNodes)

#should this test if it is a graph or if it found shortest path
def is_a_graph(graph):
    "is a graph if "

@pytest.fixture
def all_cases(one_node, random_graph):
    "bring all cases together"
    return[(one_node[0],one_node[1],one_node[2]), (random_graph[0],random_graph[1],random_graph[2])]

@pytest.mark.parametrize("algorithm_name",['dijkstraStrategy()','AStarStrategy()'] )

#[dijkstraStrategy(),AStarStrategy()]
# def process_graph(processingStrategy: GraphAlgoInterface):
#     shortestPath = processingStrategy.execute(graph, 1, 10)
#     return shortestPath

def test_algorithms(algorithm_name, all_cases):
    allCounts = []
    for graph in all_cases:
        print("----------------------paths--------------------")
        for algo in algorithm_name:
            path, count = algo.execute(graph[0], graph[1], graph[2])
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


#test_algorithms([dijkstraStrategy(), AStarStrategy()],all_cases)
