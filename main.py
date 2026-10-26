import requests
from flask import Flask, render_template
from datetime import datetime as dt

today = dt.now().date()

app = Flask(__name__)
post_url = "https://api.npoint.io/ac40c68f05791b01b40a"
response = requests.get(post_url).json()

@app.route("/")
def home():
    return render_template("index.html", response=response, date=today)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:post_id>")
def post(post_id):
    requested_post = None
    for blog_post in response:
        if blog_post["id"] == post_id:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)