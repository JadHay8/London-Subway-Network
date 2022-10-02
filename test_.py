from src.Graphing.Graph import Graph
from src.Algorithms.AlgorithmsStrategy import *
import pytest
import random


#do We Need to test for 1 node?
# @pytest.fixture
# def one_node():
#     graph = graph(1)
#     graph.add_edge(1,1,2,5)
#     graph.add_node_loc(1, 50, 1)
     
#     return [graph,1,1]

@pytest.fixture
def random_graph():
    graph = Graph(11)
    graph.add_edge(1,2,5,1)
    graph.add_edge(2,4,5,1)
    graph.add_edge(1,3,1,1)
    graph.add_edge(3,4,1,1)
    graph.add_edge(4,5,2,1)
    graph.add_edge(5,6,2,1)
    graph.add_edge(6,7,2,1)
    graph.add_edge(7,8,2,1)
    graph.add_edge(8,9,2,1)
    graph.add_edge(9,10,2,1)
    
    return [graph,1,10]

@pytest.fixture
def all_cases(random_graph):
    "bring all cases together"
    return [random_graph]



def test_dijstra_pathFinding( all_cases):
    for case in all_cases:
        path, count, time = DijkstraStrategy().execute(case[0],case[1],case[2])
        assert path == ([1,3,4,5,6,7,8,9,10], 14)
        # print("----------------------paths--------------------")
        # for algo in strategy:
        #     path, count, time = algo.execute(case[0], case[1], case[2])
        #     assert path == [1,3,4,5,6,7,8,9,10]


    return None
    








#figure out the return type of graph

# @pytest.fixture
# def empty_graph() -> dict():
#     graph = Graph(0)
#     return (graph, 0, 0)

# @pytest.fixture
# def one_node():
#     value = []
#     graph = Graph(1)
#     graph.add_edge(1, 1 ,random.randint(1,3), random.randint(1,13))
#     graph.add_node_loc(1,  random.uniform(-0.7,0.7), random.uniform(51,52)) 

#     value[0] = graph
#     value[1] = 1
#     value[2] = 1
#     return value

# @pytest.fixture
# def random_graph():
#     value = []
#     numNodes = random.randint(1,50)
#     graph = Graph(numNodes)
#     for i in range(1,numNodes):
#         #print(graph.print_adj_list())
#         if(i == 1):
#             continue
#         graph.add_node_loc(i,  random.uniform(-0.7,0.7), random.uniform(51,52))
#         graph.add_edge(i, random.randint(1,i-1),random.randint(1,3), random.randint(1,13))

#     value = [graph, 1, numNodes]
#     return value



# @pytest.fixture
# def all_cases(random_graph):
#     "bring all cases together"
#     return [ random_graph]

# #[dijkstraStrategy(),AStarStrategy()]
# @pytest.mark.parametrize("algorithm_name",["dijkstraStrategy","AStarStrategy"])


# # def process_graph(processingStrategy: GraphAlgoInterface):
# #     shortestPath = processingStrategy.execute(graph, 1, 10)
# #     return shortestPath

# #should this test if it is a graph or if it found shortest path
# def found_path(graph):
#     return True

# def test_found_path(random_graph):
#     assert found_path(random_graph)


# def test_algorithms(algorithm_name, all_cases):
#     return None
    
    # #algo = 
    # allCounts = []
    # for graph in all_cases:
    #     print("----------------------paths--------------------")
    #     for algo in algorithm_name:
    #         path, count = algo.execute(graph[0], graph[1], graph[2])
    #         print(path)
    #         allCounts.append(count)
    # dCount = []
    # aCount = []

    # for count in range(len(allCounts)):
    #     if count % 2 == 1:
    #         dCount.append(allCounts[count])
    #     if count %2 == 0:
    #         aCount.append(allCounts[count])
    # return dCount, aCount


