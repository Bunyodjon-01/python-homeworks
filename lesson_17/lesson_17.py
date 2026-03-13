## merge and join
import sqlite3
import csv

import pandas as pd

with sqlite3.connect('data/chinook.db') as connection:
    df_customers = pd.read_sql('select * from customers', con = connection)
    df_invoices = pd.read_sql('select * from invoices', con = connection)

df_joined = pd.merge(df_customers, df_invoices, how='inner', on='CustomerId')
df_joined.head()

numbers = df_joined.groupby(by=['FirstName', 'LastName'])['InvoiceId'].count()

## Outer Join on Movie Data

df_movie = pd.read_csv('data/movie.csv')
df_movie.head()
df_color = df_movie[['director_name', 'color']]
df_critic = df_movie[['director_name', 'num_critic_for_reviews']]
df_color.head()
df_critic.head()
df_left = pd.merge(df_color, df_critic, on='director_name', how='left')
df_full = pd.merge(df_color, df_critic, on='director_name', how='outer')
df_left.shape
df_full.shape

## Grouping and Aggregating
df_titanic = pd.read_excel('data/titanic.xlsx')
print(df_titanic)
df_pclass = df_titanic.groupby(by='Pclass').agg({'Fare':'sum', 'PassengerId':'count', 'Age':'mean'})
print(df_pclass)

df_multilevel = df_movie.groupby(by=['color', 'director_name']).agg({'num_critic_for_reviews':'sum', 'duration':'mean'})

needed_columns = ['Year', 'Month', 'ArrDelay', 'DepDelay']
df_flights = pd.read_parquet('data/flights', columns=needed_columns)
df_flights.head(50)

df_flights['ArrDelay'] = pd.to_numeric(df_flights['ArrDelay'], errors='coerce')
df_flights['DepDelay'] = pd.to_numeric(df_flights['DepDelay'], errors='coerce')

df_periodic = df_flights.groupby(by=['Year', 'Month']).agg(
    avg_arrival = ('ArrDelay', 'mean'),
    max_dep_delay = ('DepDelay', 'max'),
    Total_flights=('Year', 'count')
    )

## Applying Functions
def passenger(age):
    if age < 18:
        return 'Child'
    else :
        return 'Adult'
df_titanic['Age_group'] = df_titanic['Age'].apply(passenger)


df_employee = pd.read_csv('data/employee.csv')
df_employee['Normalized salaries']=df_employee.groupby(by='DEPARTMENT')['BASE_SALARY'].transform(lambda x: (x-x.min())/(x.max()-x.min()))


def mov_category(duration):
    if duration<60:
        return 'Short'
    elif duration>60 and duration<120:
        return 'Medium'
    else:
        return 'Long'
df_movie['Duration_Category'] = df_movie['duration'].apply(mov_category)

## Using pipe
def filter_survivors(df):
    return df[df['Survived'] == 1].copy()

def fill_missing_age(df):
    df['Age'] = df['Age'].fillna(df['Age'].mean())
    return df

def calculate_fare_per_age(df):
    df['Fare_Per_Age'] = df['Fare'] / df['Age']
    return df

final_titanic = (
    df_titanic
    .pipe(filter_survivors)
    .pipe(fill_missing_age)
    .pipe(calculate_fare_per_age)
)

final_titanic.head()

def filter_high_delay(df):
    return df[df['DepDelay'] > 30].copy()

def calc_delay_per_hour(df):
    df['Delay_Per_Hour'] = df['DepDelay'] / (df['Scheduled_Duration'] / 60)
    return df

final_flights = (
    df_flights
    .pipe(filter_high_delay)
    .pipe(calc_delay_per_hour)
)