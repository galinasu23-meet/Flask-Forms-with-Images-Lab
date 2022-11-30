from flask import Flask, render_template, url_for, request, redirect
from flask import session as login_session
import pyrebase
import os

Config = {
  apiKey: "AIzaSyCNjzcYiTKZe2nyQxhw_UfbEhbPk7Ki17I",
  authDomain: "meet-21653.firebaseapp.com",
  databaseURL: "https://meet-21653-default-rtdb.europe-west1.firebasedatabase.app",
  projectId: "meet-21653",
  storageBucket: "meet-21653.appspot.com",
  messagingSenderId: "1082594692785",
  appId: "1:1082594692785:web:d897a71e121216567a5c90",
  measurementId: "G-DYQ56JFKE9"
  databaseURL : "https://meet-21653-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__)
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files

UPLOAD_FOLDER = 'static/images/posts'
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']


#####


@app.route('/')  # '/' for the default page
def home():
    return render_template('index.html')


@app.route('/add_post')  # '/' for the default page
def add_post():
    return render_template('add_post.html')


if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
