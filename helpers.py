from flask import render_template
import datetime

def apology(message, code=400):

    # Render message as an apology to user, pass error code and message
    return render_template("apology.html", code=code, message=message)
    

# function for determining if a given time is within a given range
def time_in_range(start, end, current):

    # split times into hours and minutes
    start = start.split(":")
    end = end.split(":")
    current = current.split(":")

    # input hours and minutes into datetime format
    start = datetime.time(int(start[0]), int(start[1]))
    end = datetime.time(int(end[0]), int(end[1]))
    current = datetime.time(int(current[0]), int(current[1]))

    # determine whether given time is within datetime-formatted range
    return start <= current <= end