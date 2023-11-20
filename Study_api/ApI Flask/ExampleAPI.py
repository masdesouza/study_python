'''
Study about API in Python using Flask

'''

import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

# Create funcionalities
@app.route('/')
def homepage():
    return "Welcome to the Study API"

@app.route('/contacts')
def get_contacts():
    return "Here is the list of contacts"

@app.route('/contacts/<string:name>')
def get_contact(name):
    table = pd.read_csv('Study_api\contacts.csv')
    for i in range(len(table)):
        if table['first_name'][i] == name:
            name = table['first_name'][i] + ' ' + table['last_name'][i]
            return jsonify({'name': name})
            #print(table.iloc[i].to_dict())
            #return jsonify(table.iloc[i].to_dict())          
            
        else:
            return "Contact not found"
''' Example:
    Get http://localhost:5000/contacts/James
    Return: {"name": "James Smith"}
'''


@app.route('/get_sales')
def get_sales():
    table = pd.read_csv('Study_api\sales.csv')
    print(table)
    total_sales = table['Vendas'].sum()
    return jsonify({'total_sales': total_sales})


# Run API
#app.run(host='0.0.0.0')
app.run(port=5000)





