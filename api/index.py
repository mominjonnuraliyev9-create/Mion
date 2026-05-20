from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
  from mion import app
