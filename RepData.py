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

#return voter info
electionresponse = requests.get('https://content-civicinfo.googleapis.com/civicinfo/v2/voterinfo?returnAllAvailableData=true&address=' + addressString + '&officialOnly=true&key=AIzaSyAehuN2vJJFqQq6rXI_dgHfH6O5at32LW4').text
election_response_info = json.loads(electionresponse)

electionInformation = election_response_info['state'][0]['electionAdministrationBody']['electionInfoUrl']
electionRegistration = election_response_info['state'][0]['electionAdministrationBody']["electionRegistrationUrl"]
electionPollingPlace = election_response_info['state'][0]['electionAdministrationBody']["votingLocationFinderUrl"]

print('Your house representative is: ' + repName)
print(repName + "'s phone number is: ")
print(repPhone)

print(repName + "'s facebook handle is: " + repFacebookHandle)
print(repName + "'s twitter handle is: " + repTwitterHandle)
print(" ")

print('Your senators are: ' + senator1Name + ' and ' + senator2Name)
print(senator1Name + "'s phone number is: ")
print(senator1Number)
print(senator1Name + "'s facebook handle is: " + senator1FacebookHandle)
print(senator1Name + "'s twitter handle is: " + senator1TwitterHandle)

print(senator2Name + "'s phone number is: ")
print(senator2Number)
print(senator2Name + "'s facebook handle is: " + senator2FacebookHandle)
print(senator2Name + "'s twitter handle is: " + senator2TwitterHandle)

print("You can find more " + userState + " election information here: " + electionInformation)
print("You can register to vote here: " + electionRegistration)
print("You can find your polling place here: " + electionPollingPlace)
