import pandas as pd

def read(path):
    df = pd.read_csv(path, sep=',')
    return df 


