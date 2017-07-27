import sys

sys.path.insert(0, './src')

from zillowapi import api, key

def getResults(address, postalCode):

    result = api.GetSearchResults(key, address, postalCode)
    address = result.full_address
    fullAddress = ("Address: " + address.street + ", " + address.city + ", " + address.state + " " + address.zipcode)
    zestimate = result.zestiamte.amount
    formattedZestimate = '{:,}'.format(zestimate)
    return("$" + formattedZestimate)
    print(fullAddress)
