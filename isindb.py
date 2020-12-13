from pymongo import MongoClient
import pprint
import bson

client = MongoClient('mongodb://10.0.0.20:27017')
db = client.ANNADSB
isins = db['OTCISINS']


def get_isin(isin):
    record = isins.find_one({"_id": isin})
    return record

def get_isin_by_asset_class(asset_class):
    record = isins.find_one({"Header.AssetClass": asset_class})
    return record

def create_isin(record):
    isins.insert(record)

if __name__ == "__main__":
    pprint.pprint(get_isin("EZMJTKLTNSF4"))


