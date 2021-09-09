import pandas as pd


def read_csv(file_path):
    data = pd.read_csv(file_path, sep=';')
    data = data.iloc[: , 1:]
    data = data.to_dict(orient='list')
    return data