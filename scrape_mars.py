from splinter import Browser
from bs4 import BeautifulSoup


def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)


def scrape():
    