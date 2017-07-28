import sys

sys.path.insert(0, './src')

from zillowapi import api, key

def getResults(address, postalCode):
    result = api.GetSearchResults(key, address, postalCode)
    zestimate = result.zestiamte.valuation_range_low
    formattedZestimate = '{:,}'.format(zestimate)
    return("$" + formattedZestimate)

def getAddress(address, postalCode):
    result = api.GetSearchResults(key, address, postalCode)
    address = result.full_address
    fullAddress = ("Address: " + address.street + ", " + address.city + ", " +
    address.state + " " + address.zipcode)
    return(fullAddress)
