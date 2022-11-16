import requests
import json

#Getting user address
userStreetAddress = input('What is your street address: ')
userZipcode = input('What is your zipcode: ')
userCity = input('What is your city: ')
userState = input('What is your state: ')

addressString = (userStreetAddress + ', ' + userZipcode + ', ' + userCity + ', ' + userState)

#return voter info
electionresponse = requests.get('https://content-civicinfo.googleapis.com/civicinfo/v2/voterinfo?returnAllAvailableData=true&address=' + addressString + '&officialOnly=true&key=AIzaSyAehuN2vJJFqQq6rXI_dgHfH6O5at32LW4').text
election_response_info = json.loads(electionresponse)

electionInformation = election_response_info['state'][0]['electionAdministrationBody']['electionInfoUrl']
electionRegistration = election_response_info['state'][0]['electionAdministrationBody']["electionRegistrationUrl"]
electionPollingPlace = election_response_info['state'][0]['electionAdministrationBody']["votingLocationFinderUrl"]

print("You can find more " + userState + " election information here: " + electionInformation)
print("You can register to vote here: " + electionRegistration)
print("You can find your polling place here: " + electionPollingPlace)