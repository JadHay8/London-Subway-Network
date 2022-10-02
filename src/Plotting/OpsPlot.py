from matplotlib import pyplot as plt
class OpsPlot:
    def plot_algoOps(self,dCount,aCount):
            fig,axes = plt.subplots()
            scope = [10, 50, 100, 250]
            axes.set(xlabel = 'Graph size', ylabel = 'Operations')
            axes.plot(scope, [y for y in dCount] [:len(scope)], '-', label="Dijkstra")
            axes.plot(scope, [y for y in aCount] [:len(scope)], '-', label="AStar")
            axes.legend()
            fig.savefig('Outputs.Operations.pdf')
            plt.show()