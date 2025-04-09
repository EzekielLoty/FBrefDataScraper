# Necessary Imports
# StringIO for html text
# BeautifulSoup for parsing
# requests for getting website data
# pandas to manipulate the data
from io import StringIO
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

# source = requests.get('https://fbref.com/en/squads/361ca564/Tottenham-Hotspur-Stats').text
html_source = "tableshtml\passing2425.txt"
source = open(html_source)
soup = BeautifulSoup(source, "html.parser")

data_table_section = soup.find_all('div', class_="table_wrapper tabbed")

tottenham_player_lists = []
table_name = []
tottenham_player_stats = None
for data in data_table_section:
    
    title = data.div.h2.text
    data_IO = StringIO(str(data))
    df = pd.read_html(data_IO)
    
    df = df[0]
    column_name_list =[]
    
    for col in df.columns.values:
        if type(col) is tuple:
            if 'Unnamed:' in col[0]:
                temp_col = col[-1]
                
            else:
                temp_col = (col[0]+col[-1])
                
            temp_col = temp_col.replace(" ","_")   
            column_name_list.append(temp_col)
                    
    if len(column_name_list) != 0:
        df.columns = column_name_list
    
    
    if "Squad Total" and "Opponent Total" in df.values:
        i = df[(df.Player == 'Squad Total')].index[0]
        a = df[(df.Player == 'Opponent Total')].index[0]
        df = df.drop(index=[i,a])
        
        
    if "Age" in df.columns.values:
        indexer=0
        for val in df["Age"]:
            if pd.isnull(val):
                df = df.drop(indexer)
                indexer+=1
                continue
            contains_number = any(char.isdigit() for char in val)
            if contains_number==False:
                df = df.drop(indexer)
                indexer+=1
                continue
            index = df[df.Age == val].index[0]
            val = val.split("-")
            days = float(val[1])/365.2425
            yrs = val[0]
            val = f"{(float(yrs)+days):.2f}"
            df.loc[index,"Age"] = val
            val = 0
            indexer+=1
            #df[(df.Age==val)].Age = val
            #print(df[(df.Age==val)])
           
        df = df.drop(columns="Matches")
        table_name.append(title)
        df = df.fillna("NULL")
        tottenham_player_lists.append(df)
        print()
        print(title)
        print(df)
    
    
   
for (table,title) in zip(tottenham_player_lists,table_name):
    title = title.replace(" ","_")
    title = title.replace(":","")
    title = title.lower()
    table.to_csv(title+".csv", index=False)

