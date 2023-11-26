''' Example API
    We want to get data from an API? Try this one: https://economia.awesomeapi.com.br/json/all
    It returns a JSON with the exchange rate of the Brazilian Real (BRL) to all other currencies.
    DOC = https://docs.awesomeapi.com.br/
    API dp IBGE = https://servicodados.ibge.gov.br/api/docs
    API do Twillo = https://www.twilio.com/docs/sms/quickstart/python
'''
# Use to interact with API's
# API to get data from AwesomeAPI
#Install requests - pip install requests
import requests
import json

exchange = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
print(exchange.status_code)
exchange_json = exchange.json()
print(exchange_json)
exchange_USD = exchange_json['USDBRL']['bid']
print(exchange_USD)
exchange_EUR = exchange_json['EURBRL']['bid']
print(exchange_EUR)
exchange_BTC = exchange_json['BTCBRL']['bid']   
print(exchange_BTC)


# API to post data from Twillo
#Install Twillo - pip install twilio












