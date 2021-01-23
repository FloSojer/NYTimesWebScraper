"""
WebSrcapper to get the latest News from the NY Times Website

Author: Florian Sojer
"""

##
# To Do
# Save text to Database
# Host to a DJango Website or Export in a PyGame or Flask WebSite

"""
Description
Main.py
    Request and get the Website with requests.get
    change the whole Site to text
    parse the whole Site to html
    select everything what the h3, h2 or span tags includes
    filter Methods, filter Useless Headlines or non-Information 

placehoder.py
    Just Placeholders for the Commandline to find errors or useless Headlines

filter.py
    filter every tag itself for Useless Information
    At some parts, i don't understand why it does it good but as long as it Works

"""

import requests, bs4
import placeholder, filter


webSte = requests.get("https://www.nytimes.com")
wholeSite = webSte.text
gottheSoup = bs4.BeautifulSoup(wholeSite, 'html.parser')

placeholder.NyTimes_starting()
getTheH3Headlines = gottheSoup.select('h3')
filter.h3HeadlinesNYT(getTheH3Headlines)

getTheH2Headlines = gottheSoup.select('h2')
filter.h2HeadlinesNYT(getTheH2Headlines)

getTheSmallheadlines = gottheSoup.select('span')
filter.smllhdLinesFiltered(getTheSmallheadlines)

#print all Headlines =  print(filter.NyTimesHeadlines)
for i in filter.NyTimesHeadlines:
    print(i)
















