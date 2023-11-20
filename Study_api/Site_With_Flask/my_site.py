'''
Study about create web site with Flask

'''
from flask import Flask

app = Flask(__name__)

# Create a URL route in our application for "/"
# route -> domain.com/contacts
# function -> contacts() Welcome to my site, is what will be displayed on the screen.

@app.route('/')
def index():
    return 'My first site in Flask.'

@app.route('/contacts') #decorator -> @
def contacts():
    return "Welcome to my site. <p>Ours contacts are:</p><p>Phone: 11 99999-9999</p><p>Email: teste@domain.com</p>"    


# Put the site on the air
if __name__ == '__main__':
    app.run(debug=True)