import matplotlib.pyplot as plt 
import numpy as np

def get_country(data):
    try:
        country = input('What country are you interesed in? =>')
        population = data[data['Country/Territory']==country]
    except ValueError as error:
        return(error)   
    return population, country

def get_population(data):
    data = data.iloc[:,5:13]

    keys = [1970,1980,1990,2000,2010,2015,2020,2022]
    values = np.flip(data.values[0])

    return keys, values

def plot(keys, values, country):
  fig, ax = plt.subplots()
  ax.bar(keys, values)
  plt.savefig(f'./imgs/{country}.png')
  plt.close()





