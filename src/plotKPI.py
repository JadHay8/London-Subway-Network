from matplotlib import pyplot as plt
from BenchmarkSpace import *

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
plt.show()