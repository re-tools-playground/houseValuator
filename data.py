import sys

sys.path.insert(0, './src')

from zillowapi import api, key

def getResults(address, postalCode):

    result = api.GetSearchResults(key, address, postalCode)
    zestimate = result.zestiamte.amount
    formattedZestimate = '{:,}'.format(zestimate)
    print("$" + formattedZestimate)


getResults()
