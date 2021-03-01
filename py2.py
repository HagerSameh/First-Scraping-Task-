import requests
from pyquery import PyQuery as pq
import pandas as pd

response = requests.get('https://www.w3schools.com/python/ref_requests_response.asp')
list_of_dict = []

if response.status_code == 200:
    selector = pq(response.text)
    table = selector('.w3-table-all.notranslate tr:contains("Try it")').items()
    #itertable = iter(table)
   # next(itertable)
    for t in table:
       # table = selector('.w3-table-all.notranslate tr').eq(i).items()
        Property_Method = t('td').eq(0).text()
        Link = 'https://www.w3schools.com/python/' + str(t('a').attr('href'))
        Desc = t('td').eq(2).text()
        dict = {
            'Property/Method' : Property_Method ,
            'Link' : Link ,
            'Descreption' : Desc
        }


        list_of_dict.append(dict)
else:
    print ('Sorry, Bad Request!')

df = pd.json_normalize(list_of_dict)
print (df)
df.to_csv('w3schools.csv' , index= False)


