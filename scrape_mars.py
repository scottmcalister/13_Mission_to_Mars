from bs4 import BeautifulSoup
import requests
from splinter import Browser
from selenium import webdriver
import pandas as pd 
import time

def init_browser():
	return Browser("chrome", headless=False)

mission_to_mars = {}

def scrape():
	broswer = init_browser

	mars_news = 'https://mars.nasa.gov/news/'
	response = requests.get(mars_news)
	browser.visit(mars_news)

	soup = BeautifulSoup(response.text, "html.parser")

	title = soup.find("div", class_="content_title").text

	mission_to_mars["headline"] = title


	browser=Browser("chrome")
	url_image = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
	browser.visit(url_image)
	html = browser.html
	soup_div = BeautifulSoup(html,'html.parser')
	image_result = soup_div.find('img', class_="thumb")
	image_src = image_result['src']
	feat_image = "https://www.jpl.nasa.gov/" + image_src

	mission_to_mars["feat_image"] = feat_image

	tweet_url = "https://twitter.com/marswxreport?lang=en"
	response = requests.get(tweet_url)
	soup_tweet = BeautifulSoup(response.text, "html.parser")
	recent_tweet = soup_tweet.find('p', class_"TweetTextSize").text

	mission_to_mars["weather_tweet"] = recent_tweet

	url_table = "https://space-facts.com/mars/"
	mars_table - pd.read_html(url_table)
	mars_table

	mars_table_df = mars_table[0]
	mars_table_df.columns = ['Fact', 'Data']
	mars_table_df

	mars_table_html = mars_table_df.to_html(header=True, index=False)
	mission_to_mars["mars_facts_table"] = mars_table_html

	url_mars = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
	broswer.visit(url_mars)
	html = browser.html
	mars_soup = BeautifulSoup(html, 'html.parser')
	hemisphere = mars_soup.find('div', class_='collapsible results')

	results = hemisphere.find('a')

	hemisphere_list = []

	for result in results:
		if result.h3:
			title = result.h3
			link = "htps://astrogeology.usgs.gov"
			print(title, link)
			browser.visit(link)
			time.sleep(2)
			image_html = browser.html
			soup_scrape = BeautifulSoup(image_html, 'html.parser') + result['href']
			soup_image = soup_scrape.find("div", calss_="downloads").find('li').a['href']
			print(soup_image)
			mars_imgs = ['title':title, 'url_image':soup_image]
			hemisphere_list.append(mars_imgs)
			print(hemisphere_list)

			cerberus = hemisphere_list[0]['img_url']
			mission_to_mars['cerberus'] = cerberus_hemisphere

			schiaparelli = hemisphere_list[1]['img_url']
			mission_to_mars['schiaparelli'] = schiaparelli_hemisphere

			syrtis_major = hemisphere_list[2]['img_url']
			mission_to_mars['syrtis_major'] = syrtis_major_hemisphere

			valles_marineris = hemisphere_list[3]['img_url']
			mission_to_mars['valles_marineris'] = valles_marineris_hemisphere

	return mission_to_mars




















