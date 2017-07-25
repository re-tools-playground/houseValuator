import sys
sys.path.insert(0, './src')

from zillowapi import api, key


address = input(
    "What is the address without zipcode?"
);
postalCode = input(
    "What is the zipcode?"
);

zestimate = api.GetZEstimate(key, address, postalCode)

print(zestimate)