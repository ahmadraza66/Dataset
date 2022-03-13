import csv
# import pandas as pd
# import numpy as np
# import nltk
# from nltk.tokenize import word_tokenize
# import re
# import unicodedata
# nltk.download('stopwords')

file=open("gcj2009.csv")
csvreader=csv.reader(file)
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
print(rows)
file.close()

# with open('gcj2009.csv', 'r') as csvfile:
#     reader = csv.reader(csvfile, skipinitialspace=True)
    
# col_list = ["username", "flines"]
# df = pd.read_csv(r"gcj2009.csv", usecols=col_list)
# #pd.read_csv(file,) 
# print(df["username"])
# print(df["flines"])
# df.to_csv(r'cities.csv')