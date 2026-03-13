import sqlite3
from collections import Counter

import pandas as pd
#part 1

## task 1


with sqlite3.connect('data/chinook.db') as connection:
    df_customers = pd.read_sql('Select * from customers',
    con = connection
    )
print(df_customers.head(10))

## task 2

df_iris = pd.read_json("data/iris.json")
print(df_iris.shape)
print(df_iris.columns)
print(df_iris.head())

## task 3
df_titanic = pd.read_excel('data/titanic.xlsx')
print(df_titanic.head())

## task 4
df_flights = pd.read_parquet('data/flights')
df_flights.info()

## task 5
df_movie = pd.read_csv('data/movie.csv')

print(df_movie.sample(10))


# part 2
## task 1
columns = [column.lower() for column in df_iris.columns]
df_iris.columns = columns
print(df_iris.columns)
df_iris_subset = df_iris[['sepal_width', 'sepal_length']]
print(df_iris_subset)

## task 2
df_over_30 = df_titanic[df_titanic['Age'] > 30]

counts = Counter(df_titanic['Sex'])

print(counts)

print(df_over_30.head())
## task 3
print(df_flights[['Origin', 'Dest', 'Carrier']])
print(df_flights['Dest'].nunique())

## task 4
df_over120 = df_movie[df_movie['duration'] > 120]
print(df_over120.sort_values(by='director_facebook_likes', ascending=False))

# part 3
## task 1
df_iris.describe()

## task 2
print(df_titanic['Age'].min())
print(df_titanic['Age'].max())
print(df_titanic['Age'].sum())

## task 3
director_likes = df_movie.groupby('director_name')['director_facebook_likes'].sum()
top_director = director_likes.idxmax()
print(top_director)

director_long = df_movie.groupby('director_name')['duration'].max()
long_director = director_long.idxmax()
print(long_director)

## task 4
df_flights = df_flights.fillna(df_flights.mean(numeric_only=True))
print(df_flights[['DepDelay', 'AirTime']].isna().sum())