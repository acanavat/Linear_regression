import pandas as pd


def load(path: str):
    data = pd.read_csv(path)
    size = data.shape
    return data
