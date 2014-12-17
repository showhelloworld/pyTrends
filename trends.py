import mechanize
from bs4 import BeautifulSoup
import re
import time
import pynotify

def function():
	browser = mechanize.Browser()
	browser.set_handle_robots(False)
	cookies = mechanize.CookieJar()
	browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
	browser.open('https://www.facebook.com')
	browser.select_form(nr=0)
	browser.form['email'] = ''
	browser.form['pass'] = ''
	response = browser.submit()

	html = response.read()
	soup = BeautifulSoup(html)

	#facebook comments ticker, trending-posts and newsfeed
	#in the html source code
	commentSoup =  soup.find(text = re.compile("_5v9v"))

	#made a html out of the commentSoup
	soup = BeautifulSoup(commentSoup)

	spanContents = soup.findAll('span', {'class' : '_5v9v'})
	spanHeads = soup.findAll('span', {'class' : '_5v0s'})

	l = len(spanHeads)

	text_file = open("Trends.txt", "w")

	span = spanHeads + spanContents

	for i in range(l):
		pynotify.init("Basic")
		n = pynotify.Notification(span[i].get_text(), span[i+l].get_text())
		n.show()

		text_file.write(span[i].get_text())

	text_file.close()

while True:
	function()
	time.sleep(900)
