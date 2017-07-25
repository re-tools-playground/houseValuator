import zillow
import os

here = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(here, './zillow_key.conf')
with open(filename, 'r') as f:
    key = f.readline().replace("\n", "")

api = zillow.ValuationApi()
