from flask_wtf import FlaskForm
from wtforms import StringField
import requests
import json
import fileFunctions
from wtforms import FloatField


class SearchByAddressForm (FlaskForm):
    addressInput = StringField('address')
    cityInput = StringField('city')
    stateInput = StringField('state')
    zipInput = StringField('zipc')

def getOwnerData(address, city, state, zipc):
    url = "https://realty-mole-property-api.p.rapidapi.com/properties"
    strAddress = address + ", " + city + ", " + state + ", " + str(zipc)
    queryString = {"address": strAddress}
    print(queryString)

    headers = {
        "X-RapidAPI-Key": "f8005bbd93msh44616702fd74021p171d2fjsn4af0e66d1dde",
        "X-RapidAPI-Host": "realty-mole-property-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=queryString).json()
    fileFunctions.save_to_file(response, "JSON_Files/ownerInfo.json")

    getInfo = fileFunctions.read_from_file("JSON_Files/ownerInfo.json")

    return getInfo

def getPriceData(address, city, state, zipc):
    url = "https://realty-mole-property-api.p.rapidapi.com/salePrice"
    strAddress = address + ", " + city + ", " + state + ", " + str(zipc)
    queryString = {"address": strAddress}
    print(queryString)

    headers = {
        "X-RapidAPI-Key": "f8005bbd93msh44616702fd74021p171d2fjsn4af0e66d1dde",
        "X-RapidAPI-Host": "realty-mole-property-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=queryString).json()
    fileFunctions.save_to_file(response, "JSON_Files/priceInfo.json")

    getInfo = fileFunctions.read_from_file("JSON_Files/priceInfo.json")

    return getInfo