from flask import Flask, request, render_template
import os
import datetime

app = Flask(__name__)   #this creates flask app

@app.route("/")
def say_hi():
    return render_template("index.html")


@app.route("/photos")
def show_photos():
    return "<h1>this is the photos page</h1>"


@app.route("/photos/<id>")
def show_specific_photo(id):
    return "<h1>this is the photos {0}</h1>".format(id)


@app.route("/cars/<fred>/image/<wilma>")
def show_car_photo(fred, wilma):
    return "<h1>You asked for image{0} for car {1}</h1>".format(wilma, fred)


@app.route("/time")
def time():
    now = datetime.datetime.now()
    return "The current time is" + now.strftime("%H:%M:%S")

@app.route("/search")
def do_search():
    return "Search Page number 8"


if __name__ == "__main__":  # if this file is being imported, do not run code below
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)
    # app.run(host='0.0.0.0',port=8080, debug=True)
