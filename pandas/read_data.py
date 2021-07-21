import pandas as pd

## read the dataframe
df = pd.read_csv("pokemon_data.csv")
df.head()

## read the columns
# print(df.columns[2])

# print(df[['Name', 'Type 1', 'HP']])

## read the rows
# print(df.iloc[0:4])

# ## read specific location
# print(df.iloc[2,1])

## fliter function
# print(df.loc[df['Type 2'] == 'Poison'])
