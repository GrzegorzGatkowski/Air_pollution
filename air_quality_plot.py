import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

import matplotlib.pyplot as plt
import seaborn as sns

def plot_air_quality(dataframe, columns, title, xlabel, ylabel, color, palette):
    """
    Plots a lineplot of the specified columns in the given dataframe.
    
    Parameters:
    - dataframe (pandas.DataFrame): the dataframe containing the data to plot
    - columns (list of str): a list of column names to plot
    - title (str): the title of the plot
    - xlabel (str): the label for the x-axis
    - ylabel (str): the label for the y-axis
    - color (str): the color to use for the lines
    - palette (str): the seaborn palette to use for the lines
    
    Returns:
    None
    """
    dataframe_plot = dataframe[columns]
    plt.figure(figsize=(10, 6))
    sns.set_palette(palette)
    sns.lineplot(data=dataframe_plot, dashes = False)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


