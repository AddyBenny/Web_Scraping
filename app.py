from flask import Flask, render_template
from flask_pymongo import flask_pymongo
import scrape_mars

app = Flask(__name__)


