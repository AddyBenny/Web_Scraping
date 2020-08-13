12 
# Web_Scraping

Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
Step 1 - Jupyter Notebook, BeautifulSoup, Pandas, Splinter and Requests.
NASA Mars News
- Scraped the NASA Mars News Site and collect the latest News Title and Paragraph Text. 
- Assigned the text to variables that you can reference later.

JPL Mars Space Images - Featured Image
- Visit the url for JPL Featured Space Image.
- Used splinter to navigate the site and find the image url for the current Featured Mars Image 
- Assigned the url string to a variable called featured_image_url.
- Saved a complete url string for this image.

Mars Facts
- Visit the Mars Facts webpage.
- Used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
- Used Pandas to convert the data to a HTML table string.

Mars Hemispheres
- Visit the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres.
- Saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. 
- Used a Python dictionary to store the data using the keys img_url and title.
- Append the dictionary with the image url string and the hemisphere title to a list. This list contain one dictionary for each hemisphere.


Step 2 - MongoDB and Flask Application
-Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
- Converted my Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of my scraping code from above and return one Python dictionary containing all of the scraped data.
- Created a route called /scrape that will import scrape_mars.py script and call your scrape function.
- Stored the return value in Mongo as a Python dictionary.
- Created a root route / that will query Mongo database and pass the mars data into an HTML template to display the data.
- Created a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements.

Tools and library used: Jupyter Notebook, BeautifulSoup, Pandas, Splinter, Requests, MongoDB, Flask Application, HTML


