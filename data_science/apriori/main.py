from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
import csv

data = []
df = pd.DataFrame()
chunksize = 10 ** 6
with pd.read_csv('./clash_royale_games_Jan_2019.csv', chunksize=chunksize) as reader:
    for chunk in reader:
        df.append(chunk)

df.head()




