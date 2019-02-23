from flask import Flask,render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return "<h1> Its my home </h1>"

@app.route("/contact")    
def cont():
    return "contact me @ : vsn.fun@gmail.com"

if(__name__ == "__main__"):
    app.run(debug =True)