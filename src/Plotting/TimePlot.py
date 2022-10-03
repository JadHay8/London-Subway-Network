from matplotlib import pyplot as plt
class TimePlot:

    def plot_algoTime(self, dTime,aTime):
            fig,axes = plt.subplots()
            scope = [10, 50, 100, 250]
            axes.set(xlabel = 'Graph size', ylabel = 'Time (Micro Seconds)')
            axes.plot(scope, [y for y in dTime] [:len(scope)], '-', label="Dijkstra")
            axes.plot(scope, [y for y in aTime] [:len(scope)], '-', label="AStar")
            axes.legend()
            fig.savefig('Outputs.Time.pdf')
            plt.show()
