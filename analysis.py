import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from plotGraphs import plot_line,plot_bar,plot_scatter

dataset = pd.read_csv("input/dataset.csv",header=0)

by_date_Confirmed = dataset.groupby('Date')["Confirmed"].sum()
by_date_Deaths = dataset.groupby('Date')["Deaths"].sum()
by_date_Recovered = dataset.groupby('Date')["Recovered"].sum()
by_date_Active = dataset.groupby('Date')["Active"].sum()
by_date = dataset.groupby('Date')["Confirmed","Deaths","Recovered","Active"].sum()
print("\t\t\t--------------------------------\t\t\t")
print("By Date :- (Rows,Columns)","=",by_date.shape,"\n")
print(by_date.dtypes,"\n")
print(by_date.describe(),"\n")
print("Total Values by date:")
print(by_date.head(),"\n")

plot_line(by_date,'Date vs Confirmed,Deaths,Recovered,Active')
plot_line(by_date.cumsum(),'Date vs Confirmed,Deaths,Recovered,Active_(Smoothened_Curve)')
plot_line(by_date_Confirmed,'Date vs Confirmed')
plot_line(by_date_Deaths,'Date vs Deaths')
plot_line(by_date_Recovered,'Date vs Recovered')
plot_line(by_date_Active,'Date vs Active')
plot_scatter(by_date,'Date vs Confirmed,Deaths,Recovered,Active_(Scatter_Plot)')

by_Country_Confirmed = dataset.groupby('Country_Region')["Confirmed"].max()
by_Country_Deaths = dataset.groupby('Country_Region')["Deaths"].max()
by_Country_Recovered = dataset.groupby('Country_Region')["Recovered"].max()
by_Country_Active = dataset.groupby('Country_Region')["Active"].max()
by_Country = dataset.groupby('Country_Region')["Confirmed","Deaths","Recovered","Active"].max()
print("\t\t\t--------------------------------\t\t\t")
print("Values by Country :- (Rows,Columns)","=",by_Country.shape,"\n")
print(by_Country.dtypes,"\n")
print(by_Country.describe(),"\n")
print("Total Values by country:")
print(by_Country.head(),"\n")

plot_bar(by_Country,'Country vs Confirmed,Deaths,Recovered,Active')
plot_bar(by_Country_Confirmed,'Country vs Confirmed')
plot_bar(by_Country_Deaths,'Country vs Deaths')
plot_bar(by_Country_Recovered,'Country vs Recovered')
plot_bar(by_Country_Active,'Country vs Active')
plot_scatter(by_Country,'Country vs Confirmed,Deaths,Recovered,Active_(Scatter_Plot)')

# print(dataset)