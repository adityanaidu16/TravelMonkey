# TravelTexas

### **DESCRIPTION**
TravelTexas is my [FBLA (Future Business Leaders of America)](https://www.fbla-pbl.org/) entry for the Coding & Programming event. The 2022 NLC Topic is as follows:
> You have been hired by your state or local area’s tourism bureau to develop
a program that suggests attractions (can be tourist attractions, restaurants,
shopping, things to do, etc.) to potential visitors. Your program will allow
users to search for attractions in the area based on desired attributes, such as
location, type of attraction, and amenities. Your program must include at least
50 attractions, and users must be able to define at least five desired attributes
to search for an attraction.

This application allows the user to define 5 distinctive filters in order to search for a fitting attractions. Based on the given filters,
the application displays attractions in Texas that fit the user's needs.


### **FEATURES**
The functionality of this program remains simple; the user inputs their desired filters in the ***Filter*** section, using the following parameters:

**Category**
- Restaurants, Outdoor Activities, Events/Shows, Shopping, Theme Parks, Landmarks, & Museums

**Cost**
- $, $$, $$$

**Location**
- Any text input

**Rating**
- ★★★+, ★★★★+, ★★★★★

**Time**
- Any time input

After the user submits their desired filters, the ***attractions*** section displays the results of Texas attractions that match the user's criteria, starting with a featured attraction before listing all of the following results. For each result, a picture is shown alongside the attraction's name, category, cost, timings, and rating in a card.

### **TECHNOLOGIES & FRAMEWORKS**
- **Python (Flask)**
    - *Flask* is a framework written in Python that is utilized for web applications. Here, it is utilized in order to combine the productivity of Python with the visual appeal of HTML and CSS
        - The *render-template* module is used to generate output from a template file based on the Jinja2 template engine (more info below)
        - The *request* module lets Flask parse incoming request data, and gives the program access to retrieve it
        
    - The *csv* module in Python allows the program to read and manipulate the most common import and export format for spreadsheets and databases -- Comma Separated Values (CSV)
    - The *datetime* module allows the program to manipulate dates and times. In this program it's used for formatting times and is part of a function that determines if a given time is within a given range

- **HTML, CSS**
    - A free, [licensed template](https://github.com/startbootstrap/startbootstrap-grayscale/blob/master/LICENSE) from [StartBootstrap](https://startbootstrap.com/theme/grayscale) provided the basic layout and beautiful CSS visuals and features, such as the smooth scrolling page animations, while I was able to easily implement the Python and HTML functionality of retrieving the filter's input, reading and filtering through the attractions CSV file, and display the corresponding results in a aesthetic, user-friendly, readable way.
- **Javascript**
    - Minimal JS is included in the [StartBoostrap template](https://startbootstrap.com/theme/grayscale)
- **Jinja2**
    - Jinja is a template engine for Python, and is utilized in this application to reduce redundancy between the layout, index, and displayattractions HTML files. Index extends layout (the base template) as the main body, while displayattractions extends index for the main content portion of the file following the filter section.
