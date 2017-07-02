import urllib2
from bs4 import BeautifulSoup
from google import search
import html2text

def connected(host='http://google.com'):
    try:
        # check connectivity with google as reference
        urllib2.urlopen(host)
        return True
    except:
        return False

def getSoup(url):
    # required header
    hdr = {'User-Agent':
           ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 '
            '(KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),
           'Accept':
           ('text/html,application/xhtml+xml,'
            'application/xml;q=0.9,*/*;q=0.8'),
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}
    # configure reuqest
    req = urllib2.Request(url, headers=hdr)
    # open the URL and get the response
    page = urllib2.urlopen(req)
    # use HTML parser in the page response
    soup = BeautifulSoup(page, "html.parser")
    # return the parse HTML
    return soup

if connected():
    link = None
    # take input from user
    text = raw_input(
    	'Enter the song name: \n')
    # generate the API request URL
    url = 'www.azlyrics.com ' + text
    for i in search(url):
    	link = i
    	break
    # if a song result is found
    if link != 'http://www.azlyrics.com/':
        soup = getSoup(link)
        # get the lyrics
        lyrics = soup.body.find(
            "div", {"class": "col-xs-12 col-lg-8 text-center"}).findAll("div")[6].prettify()
        # print final lyrics
        print html2text.html2text(lyrics)
    else:
        print "Song not found"
else:
    print ('No Internet connectivity. '
           'PLease check your network and try again\n')
