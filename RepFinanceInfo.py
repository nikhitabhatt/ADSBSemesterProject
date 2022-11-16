import requests
import json

#this first part uses the FEC api to get the candidateID, which will be used in another API to get more information
firstName = input('What is the official first name: ')
lastName = input('What is the official last name: ')
inputparty = input('What is the official party: ')

if (inputparty == 'Democrat'):
    party = 'DEM'


if (inputparty == 'Republican'):
    party = 'REP'

FECresponse = requests.get('https://api.open.fec.gov/v1/candidates/?party=DEM&sort_null_only=false&name=' + firstName + '%20' + lastName + '&sort_nulls_last=false&sort_hide_null=false&sort=name&page=1&api_key=Q2YakfyKjQVZbWdSuz7bNcZpnGDUgsnnZmG87UA8&per_page=20').text
FECresponse_info = json.loads(FECresponse)

candidateID = FECresponse_info['results'][0]['candidate_id']

financeInfo = requests.get('https://www.opensecrets.org/api/?method=candIndByInd&cid=H6MD08457&cycle=2020&ind=K02&apikey=403edab963f60bff8dcf08004bfce7f6')
print (financeInfo)