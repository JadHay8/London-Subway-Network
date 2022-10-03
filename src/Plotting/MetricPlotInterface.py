from abc import ABC, abstractmethod

class MetricPlotInterface(ABC):
    @abstractmethod
    def plot_graph(self, metric1, metric2):
        """Method to plot graph given data using matplotlib"""
        pass