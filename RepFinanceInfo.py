import requests
import json
##key: 403edab963f60bff8dcf08004bfce7f6

##this first part uses the FEC api to get the candidateID, which will be used in another API to get more information
firstName = input('What is the official first name: ')
lastName = input('What is the official last name: ')
inputparty = input('What is the official party: ')
officialState = input('What is the state (please enter two letters (ex. MD)')

if (inputparty == 'Democrat'):
    party = 'DEM'


if (inputparty == 'Republican'):
    party = 'REP'

FECresponse = requests.get('https://api.open.fec.gov/v1/candidates/?party=' + party + '&sort_null_only=false&name=' + firstName + '%20' + lastName + '&sort_nulls_last=false&sort_hide_null=false&sort=name&page=1&api_key=Q2YakfyKjQVZbWdSuz7bNcZpnGDUgsnnZmG87UA8&per_page=20').text
FECresponse_info = json.loads(FECresponse)

candidateID = FECresponse_info['results'][0]['candidate_id']


rcpid = ""

officialState = input('What is the state (please enter two letters (ex. MD)')


##used to get the rcip id so we can use this to find campaign spending information
financeInfo = requests.get('http://www.opensecrets.org/api/?method=getLegislators&id=' + officialState + '&apikey=403edab963f60bff8dcf08004bfce7f6&output=json').text
finance_response_info = json.loads(financeInfo)
for v in finance_response_info["response"]:
    for a in finance_response_info["legislator"]:
        for b in finance_response_info["@attributes"][0]:
            print(b["lastname"])
    ##f v["lastname"] == lastName:
       ## rcpid = v["cid"]


        

##used to get the top 10 industries that contributed to a candidates campaign
top10 = requests.get('https://www.opensecrets.org/api/?method=candIndustry&cid=N00029147&cycle=2020&apikey=403edab963f60bff8dcf08004bfce7f6&output=json').text
top10industries = json.loads(top10)

##used to get the top 10 campaign donors to a campaign
top10d = requests.get('https://www.opensecrets.org/api/?method=candContrib&cid=N00007360&cycle=2020&apikey=403edab963f60bff8dcf08004bfce7f6&output=json').text
top10donors = json.loads(top10d)

