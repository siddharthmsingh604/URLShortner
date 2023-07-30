import random
import string
from flask import Flask, render_template, redirect,url_for, request

app = Flask(__name__)
shortened_urls_dict = {}

def genShortURL(length=6):
    chars = string.ascii_letters + string.digits
    shortened_url = "".join(random.choice(chars) for _ in range(length))
    return(shortened_url)

@app.route("/", methods =["GET", "POST"])
def index():
    if(request.method == "POST"):
        input_url = request.form['input_url']
        shortened_url = genShortURL()
        while(shortened_url in shortened_urls_dict):
            shortened_url = genShortURL()
        shortened_urls_dict[shortened_url] = input_url
        return(f"Shortened URL: {request.url_root}{shortened_url}")
    return(render_template("index.html"))

@app.route("/<shortened_url>")
def divertedURL(shortened_url):
    input_url = shortened_urls_dict.get(shortened_url)
    if(input_url):
        return(redirect(input_url))
    else:
        return("URL not found", 404)


if __name__ == "__main__":
    app.run(debug=True)