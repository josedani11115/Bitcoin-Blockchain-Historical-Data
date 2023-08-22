import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, to_datetime
import ydata_profiling as pp
import seaborn as sns
import warnings
from typing import Union, List, Any, Dict
import os


np.random.seed(42)

data_csv = r'D:\USER\Desktop\Ejercicios\Ciencia de datos\dataset.csv'


#Read dataset
full_data = pd.read_csv(data_csv)

#firts 5 lines
df_head = full_data.head()
#All data types
df_info = full_data.info()

""""
#EDA RENDER HTML
Render = pp.ProfileReport(full_data)
Render.to_file("data_profile_report.html")  # Save the report to an HTML file 
""" 


# TRANSACTION SIZE 


def plot_transaction(x: Union[List[Any], Series], y: Union[List[Any], Series], ylabel: str, title: Union[str, None] = None):
    fig = plt.figure(figsize=(8, 4))
    plt.plot(x, y)
    plt.ylabel(ylabel)
    plt.xticks( rotation=25 )
    plt.title(title if title is not None else "")
    plt.show()  

full_data["datetime"] = to_datetime(full_data["timestamp"], unit="s")  # <---- Understands the timestamp of data in milliseconds transforming in to years  

print(full_data.tail() , full_data.describe() , full_data.info()) # <---- EDA MANUAL

plot_transaction(x=full_data["datetime"], y=full_data["height"], ylabel="Block Number") # <---- Assiging the parameters of the data 