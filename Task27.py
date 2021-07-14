import requests
import bs4
import pandas as pd
url = 'https://www.worldometers.info/coronavirus/country/india/'
result = requests.get(url)
soup = bs4.BeautifulSoup(result.text,'lxml')
cases = soup.find_all('div' ,class_= 'maincounter-number')
data = []
for i in cases:
     span = i.find('span')
     data.append(span.string)
 print(data)
df = pd.DataFrame({"CoronaData": data})
 # Naming the coloumns
df.index = ['TotalCases', ' Deaths', 'Recovered']
 # Exporing data into Excel
df.to_csv('Corona_Data.csv')