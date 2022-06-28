from flask import Flask, render_template, request
import requests
from geopy.geocoders import Nominatim
import time
import os

# import python functions from helpers.py
from helpers import apology, convertType, formatAttractionsList, formatImage

# Configure flask application
app = Flask(__name__)

# import Google Maps API Key (stored as hidden environment variable)
API_KEY = os.environ.get('API_KEY')

# render index.html by default 
@app.route('/')
def index():
    return render_template('index.html', API_KEY=API_KEY)

# function for filtering attractions
@app.route("/", methods=["GET", "POST"])
def attractions():
    # User reach route via filter section POST (as by submitting a form via POST)
    if request.method == "POST" and 'category_response' in request.form:
        
        # toggle "show more" button visibility
        show_more = True

        # initialize global variables
        global category, cost, location, rating, open, url, attractions_list, request_time

        # request user input from HTML form
        category = request.form.get("category_response")
        cost = request.form.get("cost_response")
        location = request.form.get("location_response")
        rating = request.form.get("rating_response")
        open = request.form.get("open_response")
        if open == 'on':
            open = "&opennow=true"
        else:
            open = ""

        try:
            # create coordinates based on inputted location
            geolocator = Nominatim(user_agent="TravelMonkey")
            locator = geolocator.geocode(location)

            lat = str(locator.latitude)
            long = str(locator.longitude)
        except:
            # return error if location does not exist (exception occurs)
            return apology("Invalid Location", 400)

        # set API endpoint url
        url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

        # first request
        r = requests.get(url + 'location=' + lat + "," + long + "&type=" + category + open + "&key=" + API_KEY)
        attractions_list = r.json()

        # print(url + 'location=' + str(locator.latitude) + "," + str(locator.longitude) + "&type=" + category + open + "&key=" + API_KEY)

        # format list of attractions
        attractions_list = formatAttractionsList(attractions_list, API_KEY)

        # filter results
        results = [row for row in attractions_list['results'] if (str(row['rating']) >= rating or rating == "Any") and (int(cost) >= row['price_level']) and (row['user_ratings_total'] > 600)]
        results = sorted(results, key=lambda d: d['user_ratings_total'], reverse=True)

        # return error message if no results are found
        if not results:
            return apology("No results found", 400)

        # start timer to prepare for second request
        request_time = time.time()

        # render displayattractions.html and pass results
        return render_template('displayattractions.html', results=results, convertType=convertType, formatImage=formatImage, show_more=show_more, API_KEY=API_KEY)

    # User reach route via show more button POST (as by submitting request via POST)
    elif request.method == "POST" and 'ShowMoreButton'in request.form:

        # toggle "show more" button visibility
        show_more = False

        # if more results are available
        if('next_page_token' in attractions_list):

            # wait for cooldown period to end
            if (time.time() - request_time < 2):
                time.sleep(2 - (time.time() - request_time))
            else:
                pass

            # second request
            r2 = requests.get(url + 'pagetoken=' + attractions_list['next_page_token'] + "&key=" + API_KEY)
            request2 = r2.json()

            # format second list of attractions
            request2 = formatAttractionsList(request2, API_KEY)
            
            # append to existing list
            attractions_list['results'] = attractions_list['results'] + request2['results']

            # if even more results are available
            if('next_page_token' in request2):
                
                # wait for cooldown period to end
                time.sleep(2)

                # third request
                r3 = requests.get(url + 'pagetoken=' + request2['next_page_token'] + "&key=" + API_KEY)
                request3 = r3.json()

                # format third list of attractions
                request3 = formatAttractionsList(request3, API_KEY)
                
                # append to existing list
                attractions_list['results'] = attractions_list['results'] + request3['results']

        # format list of attractions
        attractions_list = formatAttractionsList(attractions_list, API_KEY)
        
        # filter results
        results = [row for row in attractions_list['results'] if (str(row['rating']) >= rating or rating == "Any") and (int(cost) >= row['price_level']) and (row['user_ratings_total'] > 600)]
        
        # sort results from most user reviews (most visited attractions)
        results = sorted(results, key=lambda d: d['user_ratings_total'], reverse=True)

        # return error message if no results are found
        if not results:
            return apology("No results found", 400)

        # render displayattractions.html and pass results
        return render_template('displayattractions.html', results=results, convertType=convertType, formatImage=formatImage, show_more=show_more, API_KEY=API_KEY)
    else:
        # render index.html until HTML filter form is submitted
        return render_template('index.html', API_KEY=API_KEY)

# render help.html when Help is clicked on nav-bar
@app.route("/help")
def help():
    return render_template('help.html')


