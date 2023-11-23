'''
Study about create web site with Flask

'''
from flask import Flask,render_template

app = Flask(__name__)

# Create a URL route in our application for "/"
# route -> domain.com/contacts
# function -> contacts() Welcome to my site, is what will be displayed on the screen.

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacts') #decorator -> @
def contacts():
    return render_template('contacts.html')  

@app.route('/users/<user_name>') #decorator -> @
def users(user_name):
    return render_template('users.html',user_name=user_name)
    

# Put the site on the air
if __name__ == '__main__':
    app.run(debug=True)


# Deploying a Flask App to Heroku
#    
