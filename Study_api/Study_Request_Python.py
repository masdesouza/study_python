'''
 Using request library to interact with API's

 '''
import requests

# Get data - GET request

# API to get data from AwesomeAPI
link = 'https://economia.awesomeapi.com.br/json/all'
#link = 'https://economia.awesomeapi.com.br/json/last/:moedas'
req = requests.get(link)

print(req)
print(req.json())
print(req.json()['USD'])
link = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
req = requests.get(link)
print(req.json())


#Examples of API's using Firebase 
# https://firebase.google.com/docs/reference/rest/database

# Create realtime database in Firebase
link = 'https://testresquestpython-default-rtdb.firebaseio.com/.json' # link to database

#Get data from database
req = requests.get(link) 
print(req.json())


#Create data in database
# Post data - POST request
requests.post(link , json= {'page' : 1,'name':  'Silvana', 'age': 38})                           
requests.post(link , json= {'page' : 2,'name': 'Pedro', 'age': 16})
requests.post(link , json= {'page' : 3,'name': 'Marcos', 'age': 42})

req = requests.get(link) 
print(req.json())

#Get data with parameters - GET request
params = {'page': 1}
req = requests.get(link, params = params)
response = req.json()
keys = list(response.keys())

     
#Update data partially in database
# Patch data - PATCH request
link_patch = 'https://testresquestpython-default-rtdb.firebaseio.com/'+keys[0]+'.json'
print(link_patch)
data = '{"name": "Silvana Amaral de Souza"}'
req = requests.patch(link_patch, data=data)
req = requests.get(link)
print(req.json())

# Delete data - DELETE request
link_delete = 'https://testresquestpython-default-rtdb.firebaseio.com/'+keys[0]+'.json'
requests.delete(link_delete)
req = requests.get(link)
print(req.json())

# Put data - PUT request - Update data replacing the previous all data
data = {'name': 'Pedro', 'age': 16}
req = requests.put(link , data=json.dumps(data))
req = requests.get(link) 
print(req.json())