import requests
import json

#Getting user address
userStreetAddress = input('What is your street address: ')
userZipcode = input('What is your zipcode: ')
userCity = input('What is your city: ')
userState = input('What is your state: ')

addressString = (userStreetAddress + ', ' + userZipcode + ', ' + userCity + ', ' + userState)

#getting the API data (this is for a house rep)
response = requests.get('https://content-civicinfo.googleapis.com/civicinfo/v2/representatives?address=' + addressString + '&includeOffices=true&levels=country&roles=legislatorLowerBody&key=AIzaSyAehuN2vJJFqQq6rXI_dgHfH6O5at32LW4').text
response_info = json.loads(response)

#returns rep name
repName = response_info['officials'][0]['name']

#returns rep phone number
repPhone = response_info['officials'][0]['phones']

#returns rep party
repParty = response_info['officials'][0]['party']


##returns rep social media handles
repFacebookHandle = response_info['officials'][0]['channels'][0]['id']

repTwitterHandle  = response_info['officials'][0]['channels'][1]['id']

#getting the API data (this is for a senator)
responseSenator = requests.get('https://content-civicinfo.googleapis.com/civicinfo/v2/representatives?address=' + addressString + '&includeOffices=true&levels=country&roles=legislatorUpperBody&key=AIzaSyAehuN2vJJFqQq6rXI_dgHfH6O5at32LW4').text
responseSenator_info = json.loads(responseSenator)

#returns first senator names + numbers
senator1Name = responseSenator_info['officials'][0]['name']
senator1Number = responseSenator_info['officials'][0]['phones']
##returns second senator names + numbers
senator2Name = responseSenator_info['officials'][1]['name']
senator2Number = responseSenator_info['officials'][1]['phones']

#returns senator social media information
senator1FacebookHandle = responseSenator_info['officials'][0]['channels'][0]['id']

senator1TwitterHandle  = responseSenator_info['officials'][0]['channels'][1]['id']

senator2FacebookHandle = responseSenator_info['officials'][1]['channels'][0]['id']

senator2TwitterHandle  = responseSenator_info['officials'][1]['channels'][1]['id']

#returns senator parties
senator1Party = responseSenator_info['officials'][0]['party']

senator2Party = responseSenator_info['officials'][1]['party']

financeInfo = requests.get('http://www.opensecrets.org/api/?method=getLegislators&id=' + userState + '&apikey=403edab963f60bff8dcf08004bfce7f6&output=json').text
finance_response_info = json.loads(financeInfo)

##returns the house cid
cid = ''
for person in finance_response_info['response']['legislator']:
    if (person['@attributes']['firstlast'] == repName) :
        cid = person['@attributes']['cid']

##used to get the top 10 industries that contributed to a house candidates campaign
top10 = requests.get('https://www.opensecrets.org/api/?method=candIndustry&cid=' + cid + '&cycle=2020&apikey=403edab963f60bff8dcf08004bfce7f6&output=json').text
top10industries = json.loads(top10)

##used to get the top 10 campaign donors to a house rep campaign
top10d = requests.get('https://www.opensecrets.org/api/?method=candContrib&cid=' + cid + '&cycle=2020&apikey=403edab963f60bff8dcf08004bfce7f6&output=json').text
top10donors = json.loads(top10d)

##returns the senate cid
sen1cid = ''
for person in finance_response_info['response']['legislator']:
    if (person['@attributes']['firstlast'] == senator1Name) :
        sen1cid = person['@attributes']['cid']

##used to get the top 10 industries that contributed to a senate campaign
sen1top10 = requests.get('https://www.opensecrets.org/api/?method=candIndustry&cid=' + sen1cid + '&cycle=2020&apikey=403edab963f60bff8dcf08004bfce7f6&output=json').text
sen1top10industries = json.loads(sen1top10)

##used to get the top 10 campaign donors to a senate campaign
sem1top10d = requests.get('https://www.opensecrets.org/api/?method=candContrib&cid=' + sen1cid + '&cycle=2020&apikey=403edab963f60bff8dcf08004bfce7f6&output=json').text
sen1top10donors = json.loads(sen1top10d)

##returns the senate cid
sen2cid = ''
for person in finance_response_info['response']['legislator']:
    if (person['@attributes']['firstlast'] == senator2Name) :
        sen2cid = person['@attributes']['cid']

##used to get the top 10 industries that contributed to a senate campaign
sen2top10 = requests.get('https://www.opensecrets.org/api/?method=candIndustry&cid=' + sen2cid + '&cycle=2020&apikey=403edab963f60bff8dcf08004bfce7f6&output=json').text
sen2top10industries = json.loads(sen2top10)

##used to get the top 10 campaign donors to a senate campaign
sen2top10d = requests.get('https://www.opensecrets.org/api/?method=candContrib&cid=' + sen2cid + '&cycle=2020&apikey=403edab963f60bff8dcf08004bfce7f6&output=json').text
sen2top10donors = json.loads(sen2top10d)