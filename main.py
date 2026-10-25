import requests
from flask import Flask, render_template

app = Flask(__name__)
post_url = "https://api.npoint.io/77362f8e1bd473f82ebd"
response = requests.get(post_url).json()

@app.route("/")
def home():
    return render_template("index.html", response=response)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)