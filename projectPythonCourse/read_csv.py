import csv 

def read(path):
    with open(path, mode='r') as csvfile:
        csvfile = csv.reader(csvfile, delimiter=',')
        header = next(csvfile)
        data = []
        for row in csvfile:
            zips = list(zip(header, row))
            data_dic = {key:value for key, value in zips}
            data.append(data_dic)
        return data    


