from flask_wtf import FlaskForm
from wtforms import StringField
import requests
import json
import fileFunctions

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
        "X-RapidAPI-Key": "2235028e3amsh2a5d115540b1d8bp1238ffjsn13c7860f3454",
        "X-RapidAPI-Host": "realty-mole-property-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=queryString).json()
    fileFunctions.save_to_file(response, "JSON_Files/propertyOwner.json")

    getInfo = fileFunctions.read_from_file("JSON_Files/propertyOwner.json")

    return getInfo

def getPriceData(address, city, state, zipc):
    url = "https://realty-mole-property-api.p.rapidapi.com/salePrice"
    strAddress = address + ", " + city + ", " + state + ", " + str(zipc)
    queryString = {"address": strAddress}
    print(queryString)

    headers = {
        "X-RapidAPI-Key": "2235028e3amsh2a5d115540b1d8bp1238ffjsn13c7860f3454",
        "X-RapidAPI-Host": "realty-mole-property-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=queryString).json()
    fileFunctions.save_to_file(response, "JSON_Files/values.json")

    getInfo = fileFunctions.read_from_file("JSON_Files/values.json")

    return getInfo