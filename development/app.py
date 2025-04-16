# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Welcome to UrbanReads Online Bookstore!"

if __name__ == "__main__":
    app.run(debug=True)
