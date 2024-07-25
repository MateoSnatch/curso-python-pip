import read_csv
import my_functions

data = read_csv.read('/home/mateo/Platzi/cursoPythonPipYEntornosVirtuales/projectPythonCourse/data.csv')
country = my_functions.get_country(data)
country_population = my_functions.get_population(country[0])
plot = my_functions.plot(country_population, country[1])
