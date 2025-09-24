# pip install pandas sqlalchemy psycopg2

# extracting the data
import pandas as pd 

#load the data
url = "https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2023-financial-year-provisional/Download-data/annual-enterprise-survey-2023-financial-year-provisional.csv"
data  = pd.read_csv("url")
print (data.head())

#transforming the data
remove_duplicates = data.drop_duplicates()
data_cleaned = remove_duplicates.dropna()
print (data_cleaned.head())

# load data into sql database
#from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://user:password@localhost:5432:mydatabase')

#load data into sql
data_cleaned.to_sql('survey_data', engine, index=False)
