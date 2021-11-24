########################
#   IMPORTS
########################

# Import modules
from flask import request, render_template
from app import app
import configparser

# Import functions from 'functions' file
from .functions import get_date

########################
#   MAIN VARS
########################

# Setup configuration file
config = configparser.ConfigParser()
config.read('configs/configs.ini')

# Read configuration file
author = config['author']['NAME']
website = config['author']['WEBSITE_URL']
git = config['author']['GIT_URL']

########################
# ROUTES
########################

# Home
@app.route('/')
def home():

    current_year = get_date()

    return render_template("public/index.html", year = current_year)

# About
@app.route('/about')
def about():

    return render_template("public/about.html", author = author, website = website, git = git)