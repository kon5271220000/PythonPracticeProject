import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://leagueoflegends.fandom.com/wiki/List_of_champions"
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

# Find the specific table

table = soup.find_all('table')[0]

#Get header row
header_row = table.find_all('tr')[0]

#Get header cell
header_cell = header_row.find_all('th')
header_title = [cell.text.strip() for cell in header_cell]

#create a dataframe
df = pd.DataFrame(columns=header_title)

#get all row in table
collum_data = table.find('tbody').find_all('tr')

#loop through the row to extract data
for row in collum_data:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
   
    if len(individual_row_data) == len(header_title):
        df.loc[len(df)] = individual_row_data



df.to_csv(r'/home/dierih/repos/PythonPracticeProject/04_WebScraper/data.csv', index=False)

