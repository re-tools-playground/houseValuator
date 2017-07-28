import sys

sys.path.insert(0, './src')

from zillowapi import api, key


def getRawResults(address, postalCode):
    result = api.GetSearchResults(key, address, postalCode)
    zestimate = result.zestiamte.valuation_range_low
    return int(zestimate)
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

def realisticSale(address, postalCode):
    baseValue = getRawResults(address, postalCode)
    realisticSaleValue = baseValue * 0.71
    formattedValue = '{:,}'.format(realisticSaleValue)
    return formattedValue


def getMaxBid(address, postalCode):
    homeValue = getRawResults(address, postalCode) * 0.71
    maxBid = homeValue * 0.67
    formattedBid = '{:,}'.format(maxBid)
    return("$" + formattedBid)
