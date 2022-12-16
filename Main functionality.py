import requests
import json
from congress import Congress
congress = Congress("UBUkraUmSFaWkkJ64CgAxwbc4PY44dXVEyVxRsey")


#Getting user address
userStreetAddress = input('What is your street address: ')
userZipcode = input('What is your zipcode: ')
userCity = input('What is your city: ')
userState = input('What is your state: ')

addressString = (userStreetAddress + ', ' + userZipcode + ', ' + userCity + ', ' + userState)

#gets recent house and senate bills
def recentHouseBills():
    introdHouse = congress.bills.recent(chamber='house', congress=111, type='introduced')
    return introdHouse

def recentSenateBills():
    introdSenate = congress.bills.recent(chamber='senate', congress=111, type='introduced')
    return introdSenate
#gets recent house and senate votes
def recentHouseVotes():
    houseVotes = congress.votes.by_month(chamber='house')
    return houseVotes

def recentSenateVotes():
    senateVotes = congress.votes.by_month(chamber='senate')
    return senateVotes

##returns all the rep info
def repName():
    return repName

def repPhone():
    return repPhone

def repParty():
    return repParty

def repFacebook():
    return repFacebookHandle

def repTwitter():
    return repTwitterHandle

def repTop10ind():
    return top10industries

def repTop10don():
    return top10donors

def repArticles():
    return repArticles

##returns all the senator 1 info

def sen1Name():
    return senator1Name

def sen1Phone():
    return senator1Number

def sen1Party():
    return senator1Party

def sen1Facebook():
    return senator1FacebookHandle

def sen1Twitter():
    return senator1TwitterHandle

def sen1top10industries():
    return sen1top10industries

def sen1top10donors():
    return sen1top10donors

def sen1articles():
    return senator1Articles

##returns all the senator 2 info

def sen2Name():
    return senator2Name

def sen2Phone():
    return senator2Number

def sen2Party():
    return senator2Party

def sen2Facebook():
    return senator2FacebookHandle

def sen2Twitter():
    return senator2TwitterHandle

def sen2top10industries():
    return sen2top10industries

def sen2top10donors():
    return sen2top10donors

def sen2articles():
    return senator2Articles

#getting the API data (this is for a house rep)
response = requests.get('https://content-civicinfo.googleapis.com/civicinfo/v2/representatives?address=' + addressString + '&includeOffices=true&levels=country&roles=legislatorLowerBody&key=AIzaSyAehuN2vJJFqQq6rXI_dgHfH6O5at32LW4').text
response_info = json.loads(response)

#returns rep name
repName = response_info['officials'][0]['name']
repl = repName.split()
repx = len(repl)
repLastName = repl.pop()


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

sen1l = senator1Name.split()
sen1x = len(sen1l)
sen1LastName = sen1l.pop()

senator1Number = responseSenator_info['officials'][0]['phones']

##returns second senator names + numbers
senator2Name = responseSenator_info['officials'][1]['name']
senator2Number = responseSenator_info['officials'][1]['phones']

sen2l = senator2Name.split()
sen2x = len(sen2l)
sen2LastName = sen2l.pop()

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
repCid = ''
for person in finance_response_info['response']['legislator']:
    if (person['@attributes']['lastname'] == repLastName) :
        repCid = person['@attributes']['cid']

##used to get the top 10 industries that contributed to a house candidates campaign
top10 = requests.get('https://www.opensecrets.org/api/?method=candIndustry&cid=' + repCid + '&cycle=2020&apikey=403edab963f60bff8dcf08004bfce7f6&output=json').text
if top10 == 'Resource not found':
    top10industries = 'Not found'
elif top10 == 'Invalid CID':
    top10industries = 'Not found'
else:
    top10industries = json.loads(top10)

##used to get the top 10 campaign donors to a house rep campaign
top10d = requests.get('https://www.opensecrets.org/api/?method=candContrib&cid=' + repCid + '&cycle=2020&apikey=403edab963f60bff8dcf08004bfce7f6&output=json').text
if top10d == 'Resource not found':
    top10donors = 'Not found'
elif top10d == 'Invalid CID10700':
    top10donors = 'Not found'
else:
    top10donors = json.loads(top10d)



##returns the senate cid
sen1cid = ''
for person in finance_response_info['response']['legislator']:
    if (person['@attributes']['lastname'] == sen1LastName) :
        sen1cid = person['@attributes']['cid']

#fix this code
##used to get the top 10 industries that contributed to a senate campaign
sen1top10ind = requests.get('https://www.opensecrets.org/api/?method=candIndustry&cid=' + sen1cid + '&cycle=2020&apikey=403edab963f60bff8dcf08004bfce7f6&output=json').text
if sen1top10ind == 'Resource not found':
    sen1top10industries = 'Not found'
elif sen1top10ind == 'Invalid CID':
    sen1top10industries = 'Not found'
else:
    sen1top10industries = json.loads(sen1top10ind)

#used to get the top 10 campaign donors to a senate campaign
sen1top10d = requests.get('https://www.opensecrets.org/api/?method=candContrib&cid=' + sen1cid + '&cycle=2020&apikey=403edab963f60bff8dcf08004bfce7f6&output=json').text
if sen1top10d == 'Resource not found':
    sen1top10donors = 'Not found'
elif sen1top10d == 'Invalid CID':
    sen1top10donors = 'Not found'
else:
    sen1top10donors = json.loads(sen1top10d)

##returns the senate cid
sen2cid = ''
for person in finance_response_info['response']['legislator']:
    if (person['@attributes']['lastname'] == sen2LastName) :
        sen2cid = person['@attributes']['cid']

##used to get the top 10 industries that contributed to a senate campaign
sen2top10 = requests.get('https://www.opensecrets.org/api/?method=candIndustry&cid=' + sen2cid + '&cycle=2020&apikey=403edab963f60bff8dcf08004bfce7f6&output=json').text
if sen2top10 == 'Resource not found':
    sen2top10industries = 'Not found'
elif sen2top10 == 'Invalid CID':
    sen2top10industries = 'Not found'
else:
    sen2top10industries = json.loads(sen2top10)

##used to get the top 10 campaign donors to a senate campaign
sen2top10d = requests.get('https://www.opensecrets.org/api/?method=candContrib&cid=' + sen2cid + '&cycle=2020&apikey=403edab963f60bff8dcf08004bfce7f6&output=json').text
if sen2top10d == 'Resource not found':
    sen2top10donors = 'Not found'
elif sen2top10d == 'Invalid CID':
    sen2top10donors = "Not found"
else:
   sen2top10donors = json.loads(sen2top10d)

#returns the latest news articles for a person
rarticles = requests.get('https://api.goperigon.com/v1/all?apiKey=08db32cd-ff74-4992-959b-3b2a0899d564&q="' + repName + '" &showReprints=false&from=2022-01-01&to=2022-01-31').text
repArticles = json.loads(rarticles)

sen1articles = requests.get('https://api.goperigon.com/v1/all?apiKey=08db32cd-ff74-4992-959b-3b2a0899d564&q="' + senator1Name + '" &showReprints=false&from=2022-01-01&to=2022-01-31').text
senator1Articles = json.loads(sen1articles)

sen2articles = requests.get('https://api.goperigon.com/v1/all?apiKey=08db32cd-ff74-4992-959b-3b2a0899d564&q="' + senator2Name + '" &showReprints=false&from=2022-01-01&to=2022-01-31').text
senator2Articles = json.loads(sen2articles)

##New stuff
introdHouse = congress.bills.recent(chamber='house', congress=111, type='introduced')
print(introdHouse)

introdSenate = congress.bills.recent(chamber='senate', congress=111, type='introduced')
print(introdSenate)

houseVotes = congress.votes.by_month(chamber='house')
print(houseVotes)

senateVotes = congress.votes.by_month(chamber='senate')
print(senateVotes)

##more new stuff
output = json.load(open(r"C:\Users\nikhi\Downloads\BioguideReps.json"))


bioguideRep = ''
for person in output:
    if (person['name']['last'] == repLastName) :
        bioguideRep = person['id']['bioguide']
print(bioguideRep)

repBills = congress.members.bills(bioguideRep, type='introduced')
print(repBills)