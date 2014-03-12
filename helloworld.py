# This simple Python script demonstrates 
# making a simple rest call to
# XigniteGlobalCurrencies -> ListCurrencies. 
# It receives JSON data from the service.
# It parses and displays the data to the console
#

#pip install requests
import requests
import json

#ensure config has the write permissions
from config import _token

#Get JSON data to format and print
def printData(jsonText):
	data = json.loads(jsonText)
	for country in data["CurrencyList"]:
		print "\nNext"
		print "Name: " + country["Name"]
		print "Symbol: " + country["Symbol"]

#make a get request to given url
def getUrl(url):
	response = requests.get(url)

	return response

base_url = "http://globalcurrencies.xignite.com/"
action = "xGlobalCurrencies.json/ListCurrencies?_token="

response = getUrl(base_url+action+_token)
printData(response.text)
