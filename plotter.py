from dataclasses import dataclass
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import _axes  # type(ax) in fig, ax = plt.subplots()
from matplotlib.figure import Figure  # type(fig) in fig, ax = plt.subplots()

@dataclass
class PlotData:
    '''
    class to pass data into plot function
    x: x axis data
    y: y axis data
    x_label: x axis label
    y_label: y axis label
    title: graph title
    '''
    x: list[float]
    y: list[float]
    x_label: str
    y_label: str
    title: str

class Plotter:
    def plot_one(self, line_data: PlotData) -> Figure:
        '''
        Plot one line on graph
        line_data: PlotData object
        '''
        fig, ax = plt.subplots()
        ax.plot(line_data.x, line_data.y)
        self.configure_plot(ax, line_data.x_label, line_data.y_label, line_data.title)
        return fig

    def plot_multiple(self, data: list[PlotData], title: str, x_label: str, y_label: str) -> Figure:
        '''
        Plot multiple lines on the same graph
        data: list of lines to plot, title of each line will be the line label
        title: title of graph
        x_label: x axis label
        y_label: y axis label
        '''
        fig, ax = plt.subplots()
        for line in data:
            ax.plot(line.x, line.y, label=line.title)
        self.configure_plot(ax, x_label, y_label, title)
        ax.legend(loc="best")
        return fig

    def configure_plot(self, ax: _axes.Axes, x_label: str, y_label: str, title: str) -> None:
        '''
        configure line data
        ax: axis
        x_label: x axis label
        y_label: y axis label
        title: graph title
        '''
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title(title)
        ax.grid()