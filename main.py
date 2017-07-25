import sys
sys.path.insert(0, './src')

from zillowapi import api, key

def getResults():
    address = "2307 Fairway Pointe Drive, League City, TX"
    postalCode = "77573"

    result = api.GetSearchResults(key, address, postalCode)
    zestimate = result.zestiamte.amount
    print(zestimate)


getResults()
