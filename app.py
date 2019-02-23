from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "bro"

@app.route("/home")
def home():
    return "Its my home"

@app.route("/contact")    
def cont():
    return "contact me @ : vsn.fun@gmail.com"
    
if(__name__ == "__main__"):
    app.run()