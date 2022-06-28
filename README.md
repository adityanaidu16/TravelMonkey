# TravelTexas

### **DESCRIPTION**
TravelMonkey is our [FBLA (Future Business Leaders of America)](https://www.fbla-pbl.org/) entry for the Coding & Programming event. The 2022 NLC Topic is as follows:
> You have been hired by your state or local area’s tourism bureau to develop
a program that suggests attractions (can be tourist attractions, restaurants,
shopping, things to do, etc.) to potential visitors. Your program will allow
users to search for attractions in the area based on desired attributes, such as
location, type of attraction, and amenities. Your program must include at least
50 attractions, and users must be able to define at least five desired attributes
to search for an attraction.

This application allows the user to define 5 distinctive filters in order to search for a fitting attractions. Based on the given filters,
the application displays attractions in a given city that fit the user's needs.


### **FEATURES**
The functionality of this program remains simple; the user inputs their desired filters in the ***Filter*** section, using the following parameters:

**Category**
- Amusement Parks, Aquariums, Campgrounds, Museums, Parks, Restaurants, Shopping, Stadiums, Tourist Attractions, and Zoos

**Cost**
- Free, $, $$, $$$, $$$$

**Location**
- Any text input (has auto-complete feature enabled by Google Maps Places API)

**Rating**
- ★★★+, ★★★★+, ★★★★★

**Open Now**
- Toggle between open now and  no preference

After the user submits their desired filters, the ***attractions*** section displays the results of attractions that match the user's criteria, starting with a featured attraction before listing all of the following results. For each result, a picture is shown alongside the attraction's name, category, cost, availability, and rating in a card.

### **TECHNOLOGIES & FRAMEWORKS**
- **Python (Flask)**
    - *Flask* is a framework written in Python that is utilized for web applications. Here, it is utilized in order to combine the productivity of Python with the visual appeal of HTML and CSS
        - The *render-template* module is used to generate output from a template file based on the Jinja2 template engine (more info below)
        - The *request* module lets Flask parse incoming request data (such as the filter form), and gives the program access to retrieve it
        
    - The *Nominatim* module from GeoPy gives the application functionality to convert a location that is entered within the city query in the filter section into geographical coordinates that can be passed through the API request.
    - The *requests* module in Python allows the program to make and send HTTP requests using Python. It is utilized in this program to make an API request using our Google Maps Places API endpoint to return a Response object containing results.
    - *os* and *dotenv* are used to securely store the sensitive API key hidden within the project.


- **HTML, CSS**
    - A free, [licensed template](https://github.com/startbootstrap/startbootstrap-grayscale/blob/master/LICENSE) from [StartBootstrap](https://startbootstrap.com/theme/grayscale) provided the basic layout and beautiful CSS visuals and features, such as the smooth scrolling page animations, while we were able to easily implement the Python and HTML functionality of retrieving the filter's input, making and filtering through an API request, and displaying the corresponding results in a aesthetic, user-friendly, readable way.
- **Javascript**
    - Minimal JS is included in the [StartBoostrap template](https://startbootstrap.com/theme/grayscale)
- **Jinja2**
    - Jinja is a template engine for Python, and is utilized in this application to reduce redundancy between the layout, index, and displayattractions HTML files. Index extends layout (the base template) as the main body, while displayattractions extends index for the main content portion of the file following the filter section.

- **Google Maps Places API**
    - The [Places API](https://developers.google.com/maps/documentation/places/web-service) is a service that returns information about places using HTTP requests. Places are defined within this API as establishments, geographic locations, or prominent points of interest.
    - Data is retrieved from the Google Cloud Platform when a request is made through a given endpoint with a designated API key
    - Places served this projects needs the most effectively, as it was free of cost, and gave us far more flexibility than competitors, allowing us to add features such as the autocomplete in the city query.
    - This was our first time utilizing an API within a full-fledged project/application before, and while there were several obstacles and hiccups, this API made it easy to navigate and solve issues due to its widespread use
