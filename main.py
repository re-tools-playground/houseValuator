import sys
sys.path.insert(0, './src')

from zillowapi import api, key


address = "3400 Pacific Ave., Marina Del Rey, CA"
postalCode = "90292"

result = api.GetSearchResults(key, address, postalCode)

print(result)
