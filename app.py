from flask import Flask, render_template, request
import csv
from datetime import datetime

# import python functions from helpers.py
from helpers import apology, time_in_range

# Configure flask application
app = Flask(__name__)

# render index.html by default
@app.route('/')
def index():
    return render_template('index.html')

# function for converting 24 hour time (from spreadsheet) to 12 hour time (to display)
@app.template_filter()
def convert_time(time):
    new_time = datetime.strptime(time, "%H:%M")
    new_time = new_time.strftime("%I:%M %p")

    # remove redundant zero if possible
    if (new_time[0] == '0'):
        new_time = new_time[1:]

    # return 12-hour-formatted time
    return new_time

# function for filtering attractions
@app.route("/", methods=["GET", "POST"])
def attractions():
    # User reach route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # request user input from HTML form
        category = request.form.get("category_response")
        cost = request.form.get("cost_response")
        location = request.form.get("location_response")
        rating = request.form.get("rating_response")
        time = request.form.get("time_response")

        # open csv file containing attractions' information
        with open('attractions.csv') as csvfile:

            # read csv file
            attractions_csv = csv.reader(csvfile)
            header = next(attractions_csv)

            # filter row-by-row for matching parameters
            results = [row for row in attractions_csv if (category == row[2] or category == "Any") and (cost == row[3] or cost == "Any") and (location.lower() == row[4].lower() or location == "") and (row[5] >= rating or rating == "Any")and (time == "" or time_in_range(row[6], row[7], time) == True)]
        
        # return error message if no results are found
        if not results:
            return apology("No results found", 400)

        # render displayattractions.html and pass results
        return render_template('displayattractions.html', results=results, convert_time=convert_time)

    else:
        # render index.html until HTML form is submitted
        return render_template('index.html')

# render help.html when Help is clicked on nav-bar
@app.route("/help")
def help():
    return render_template('help.html')


