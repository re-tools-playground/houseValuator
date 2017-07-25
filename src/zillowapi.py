import zillow

with open("../bin/zillow_key.conf", 'r') as f:
    key = f.readline().replace("\n", "")

api = zillow.ValuationApi()