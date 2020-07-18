from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver
import pymongo
import time
import os



def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # Visit visitcostarica.herokuapp.com
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page Nasa Mars News into Soup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    news_title = soup.find_all('div', class_='content_title')
    news_title[1].get_text()
    news_p = soup.find_all('div', class_='article_teaser_body')
    news_p[0].get_text()
    
    #scrape page JPL mars space into soup
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    find = browser.find_by_id('full_image')
    find.click()
    footer = soup.find('footer').find('a')
    footer
    featured_image_url = 'https://www.jpl.nasa.gov' + footer.attrs['data-fancybox-href']
    featured_image_url
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    #url = 'https://www.jpl.nasa.gov'
    #src = url + src
    
    
   #scrape Mars facts 
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    html_table = df.to_html()
    mars_facts = html_table
   

    #scrape Mars Hemisphere
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    html = browser.html
    soup =bs(html, 'html.parser')
    results = soup.find_all('div', class_='item')

    hemispere_image_url = []
    for i, result in enumerate(results):
        
        h3 = result.find('h3')
        h3 = h3.text
        link = result.find('a')
        href = link['href']
        url = 'http://astrogeology.usgs.gov'+ href
        
        hemispere_image_url.append({"title":h3,
        "url":url})


    # Store data in a dictionary
    mars_data = {
        "mars_new_title": news_title,
        "mars_paragraph": news_p,
        "mars_image":  featured_image_url,
        "mars_table": mars_facts,
        "images": hemispere_image_url
    }

    # Close the browser after scraping
    browser.quit()
    return mars_data


