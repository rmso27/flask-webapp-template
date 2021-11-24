########################
#   IMPORTS
########################

# Import modules
import datetime

# Function to get current date (year)
def get_date():

    current_date = datetime.datetime.now()
    current_year = current_date.year

    return current_year