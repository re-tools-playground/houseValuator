import sys
sys.path.insert(0, './src')

from zillowapi import api, key


address = "2307 Fairway Pointe Drive, League City, TX"
postalCode = "77573"

result = api.GetSearchResults(key, address, postalCode)
zestimate = result.get_dict()
print(zestimate)
