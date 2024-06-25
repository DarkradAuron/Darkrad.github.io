#Data Clean Up Automation Using Python
#Python 3.X Compatible
#Source: https://www.espncricinfo.com/records/highest-career-batting-average-282910
#Clean up data using Pandas in Python
import pandas as pd

#Reading the file into the dataframe
df = pd.read_csv("Cricket_Test_Sample.csv")

#Updating multiple column names to be less confusing 
df = df.rename(columns = {'MAT':'Matches','NO':'Not_Outs', 'HS':'Highest_Inns_Score', 'BF':'Balls_Faced', 'SR':'Batting_Strike_Rate'}) 

#Checking for duplicates either coming up as TRUE or FALSE
df.duplicated()

#Checking individual records for duplicates using Player to pull all the duplicate records
df[df['Player'].duplicate()==1]

#Checking the records by the player name from the previous search
df[df['Player'].isin(['GS Sobers (WI)', 'SR Tendulkar (IND)'])]

#Dropping the duplicates
df = df.drop_duplicates()

#Checking the split of the Span column by spliting on the '-' to make sure it is what we want
df['Span'].str.split(pat = '-')

#Spliting the Span column to show the first year a player has played
df['Rookie_Year'] = df['Span'].str.split(pat = '-').str[0]

#Spliting the Span column to show the final year a player has played
df['Final_Year'] = df['Span'].str.split(pat = '-').str[1]

#Dropping the Span column since it is no longer needed
df.drop(['Span'], axis = 1)

#Checking the data types of each column in the dataframe 
df.dtypes

#Cleaning up and spliting columns that have values with special characters in them that don't belong there like * or +
df['Highest_Inns_Score'] = df['Highest_Inns_Score'].str.split(pat = '*').str[0]

df['Balls_Faced'] = df['Balls_Faced'].str.split(pat = '+').str[0]

#Changing the datatypes of columns to fit their values so it is less confusing and easier for other users to use
df['Highest_Inns_Score'] = df['Highest_Inns_Score'].astype('int')

df['Batting_Strike_Rate'] = df['Batting_Strike_Rate'].astype('float')

df['Balls_Faced'] = df['Balls_Faced'].astype('float')

#Creating a column that gives the Career Length of each player by using a simple calculation and putting it into a new column close to our Rookie_Year and Final_Year columns
df['Career_Length'] = df['Final_Year'] - df['Rookie_Year']

#Seperating the Country from the Player name and putting it into a new column while removing it from the Player name
df['Country'] = df['Player'].str.split(pat = '(').str[1]

df['Country'] = df['Country'].str.split(pat = ')').str[0]

df['Player'] = df['Player'].str.split(pat = '(').str[0]