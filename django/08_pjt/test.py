import csv
import numpy as np
import pandas as pd

df = pd.read_csv('test_data.CSV', encoding='cp949')
df.fillna(value='Null', inplace=True)
print(df)