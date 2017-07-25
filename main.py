import sys
sys.path.insert(0, './src')

from zillowapi import api, key


address = raw_input("What is the address without the zipcode?")
postalCode = raw_input("What is the zipcode?")

result = api.GetSearchResults(key, address, postalCode)
zestimate = result.get_dict()


print(zestimate)
