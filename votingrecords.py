import requests
import json
from congress import Congress
congress = Congress("UBUkraUmSFaWkkJ64CgAxwbc4PY44dXVEyVxRsey")

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

introdHouse = congress.bills.recent(chamber='house', congress=111, type='introduced')
print(introdHouse)

introdSenate = congress.bills.recent(chamber='senate', congress=111, type='introduced')
print(introdSenate)

houseVotes = congress.votes.by_month(chamber='house')
print(houseVotes)

senateVotes = congress.votes.by_month(chamber='senate')
print(senateVotes)


