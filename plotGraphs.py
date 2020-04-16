import pandas as pd
import matplotlib.pyplot as plt

def plot_line(data,name):
    data.plot.line(figsize=(25,12.5))
    plt.legend(loc = 'best')
    plt.title(name)
    plt.xlabel(name.split(" ")[0])
    plt.ylabel(name.split(" ")[-1])
    plt.savefig("output/"+name+".png")
    plt.gcf().clear()

def plot_scatter(data,name):
    data.plot.scatter(x="Confirmed",y="Deaths",c="Recovered",colormap='viridis',figsize=(25,12.5))
    plt.title(name)
    plt.savefig("output/"+name+".png")
    plt.gcf().clear()

def plot_bar(data,name):
    data.plot.bar(figsize=(50,25))
    plt.legend(loc = 'best')
    plt.title(name)
    plt.xlabel(name.split(" ")[0])
    plt.ylabel(name.split(" ")[-1])
    plt.savefig("output/"+name+".png")
    plt.gcf().clear()

