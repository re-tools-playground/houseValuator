import sys

sys.path.insert(0, './src')

from zillowapi import api, key

def getResults():
    address = raw_input("Address: ")
    postalCode = raw_input("Zip Code: ")

    result = api.GetSearchResults(key, address, postalCode)
    zestimate = result.zestiamte.amount
    formattedZestimate = '{:,}'.format(zestimate)
    print(formattedZestimate)


getResults()
