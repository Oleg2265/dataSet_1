import pandas as pd
df = pd.read_csv('countries of the world.csv')
#print(df.info())
print(pd.isnull(df["Net migration"]))
df["Net migration"].fillna(0, inplace = True)
print(pd.isnull(df["Net migration"]))

def make_migration(migration):
    if migration[-1] == "-":
        return float(migration[1:])
    return -1