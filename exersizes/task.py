import pandas as pd
import csv

df = pd.read_csv("../120 Olympics/athlete_events.csv", header=None, sep='\s+')
df.columns = ['ID', 'Name', 'Sex','Age', 'Height', 'Weight', 'Team', 'NOC', 'Games', 'Year' ]
n=1
