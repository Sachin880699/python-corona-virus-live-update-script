'''import requests

url = "https://thevirustracker.com/free-api?global=stats"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

sachin = response.text.encode('utf8')


data = open('file.txt','w')
data.write(str(sachin))
data.close()'''


# load text
file = open('file.txt', 'rt')
text = file.read()
file.close()
# split based on words only
import re
words = re.split(r'\W+', text)
#-----this is for total cases----
total_cases = words.index('total_cases')+1
print('total_cases',words[total_cases])

#------this is for total_recovered

total_recovered = words.index('total_recovered')+1
print('total_recovered',words[total_recovered])

#------this is for the total_deaths

total_deaths = words.index('total_deaths')+1
print('total_deaths',words[total_deaths])















