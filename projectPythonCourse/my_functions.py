import matplotlib.pyplot as plt 

def get_country(data):
    try:
        country = input('What country are you interesed in? =>')
        population = list(filter(lambda x: x['Country/Territory'] == country, data))
    except ValueError as error:
        return(error)   
    return population[0], country

def get_population(data):
    keys = ['2020 Population', '2015 Population', '2010 Population', 
            '2000 Population', '1990 Population', '1980 Population', '1970 Population']
    year_labels = [2022, 2020, 2015, 2010, 2000, 1990, 1980, 1970]
    population = [data[value] for value in keys]
    year_labels.reverse()
    population.reverse()

    country_population = {key:value for key,value in zip(year_labels,population)}
    return country_population

def plot(data, country):
  fig, ax = plt.subplots()
  ax.bar(data.keys(), data.values())
  plt.savefig(f'./imgs/{country}.png')
  plt.close()





