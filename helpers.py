from flask import render_template

# error message
def apology(message, code):

    # Render message as an apology to user, pass error code and message
    return render_template("apology.html", code=code, message=message)
    
# format attraction types
def convertType(type):
    if type == "amusement_park":
        return "Amusement Park"
    elif type =="aquarium":
        return "Aquarium"
    elif type == "campground":
        return "Campground"
    elif type == "museum":
        return "Museum"
    elif type == "park":
        return "Park"
    elif type == "restaurant":
        return "Restaurant"
    elif type == "shopping_mall":
        return "Shopping"
    elif type =="stadium":
        return "Stadium"
    elif type =="tourist_attraction":
        return "Tourist Attraction"
    elif type =="zoo":
        return "Zoo"
    else:
        return None

# format images for high resolution/quality
def formatImage(img):
    return img.replace('maxwidth=400', 'maxwidth=1280')

# format list of attractions/results
def formatAttractionsList(list, API_KEY):
    for item in list['results']:
        # if price level exists, don't change
        try:
            item['price_level'] = item['price_level']

        # if price level doesn't exist, change it to the following:
        except:
            # set price level of parks to free
            if 'park' in item['types'] or 'campground' in item['types']:
                item['price_level'] = 0
            
            # set price level of museums, aquariums, and amusement parks to 3
            elif 'museum' in item['types'] or 'aquarium' in item['types'] or 'amusement_park' in item['types']:
                item['price_level'] = 3
            
            # set everything else to 2
            else:
                item['price_level'] = 2
        
        # format image source url
        try:
            item['image_source_primary'] = str("https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photo_reference=" + item['photos'][0]['photo_reference'] + "&key=" + API_KEY)
        except:
            item['image_source_primary'] = "..."

        # ensure rating exists (to avoid further errors when filtering)
        try:
            item['rating'] = item['rating']
        except:
            item['rating'] = 0
        
        # ensure # of ratings exists
        try:
            item['user_ratings_total'] = item['user_ratings_total']
        except:
            item['user_ratings_total'] = 0

        # format image attribution
        try:
            item['image_attribution'] = str(item['photos'][0]['html_attributions']).replace("<a", "<a class='mb-0 text-gray-50 fs-7' target='_blank'")
            item['image_attribution'] = item['image_attribution'][2:-2]
        except:
            item['image_attribution'] = "<p class='mb-0 mt-0 text-gray-50 fs-7'>Unavailable</p>"

    # return formatted list of attractions
    return list