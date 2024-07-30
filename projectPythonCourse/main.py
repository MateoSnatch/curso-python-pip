import read_csv
import my_functions
import numpy as np

data = read_csv.read('./data.csv')
country = my_functions.get_country(data)
country_population = my_functions.get_population(country[0])
plot = my_functions.plot(country_population[0], country_population[1], country[1])
