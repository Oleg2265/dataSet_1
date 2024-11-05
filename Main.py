import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv('countries of the world.csv')

#df["Population"].mean()
#print(df["Population"].mean())
#28,740,284.7




df["Area (sq. mi.)"].mean()
print(df["Area (sq. mi.)"].mean())
#598227

df["Area (sq. mi.)"].value_counts().plot(kind = 'pie')





#def make_pop(Population):
    #if Population[-1] == "-":
        #return float(Population[1:])
    #return -1

