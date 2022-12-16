import requests
import json



repLastName = 'Raskin'

output = json.load(open(r"C:\Users\nikhi\Downloads\BioguideReps.json"))


bioguideRep = ''
for person in output:
    if (person['name']['last'] == repLastName) :
        bioguideRep = person['id']['bioguide']
print(bioguideRep)