from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
  me = {
    "first_name": "Jaden",
    "last_name": "Sherpa",
    "is_online": True,
    "hobbies": "biking...",
  }
  
  return me 