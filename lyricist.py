import urllib2
import json
from BeautifulSoup import BeautifulSoup

API_KEY = 'your API key here'

def connected(host='http://google.com'):
    try:
        # check connectivity with google as reference
        urllib2.urlopen(host)
        return True
    except:
        return False
if connected():
    # take input from user
    text = raw_input('Enter the artist name followed by the song or just the song name: \n')
    # convert input to lowercase for easy comparison
    textCopy = text.lower()
    # strip extra spaces
    text = text.strip();
    # format the string to a query
    text = text.replace(' ','%20')
    # generate the API request URL
    url = 'http://api.lyricsnmusic.com/songs?api_key='+API_KEY+'&q='+text
    # required header
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                       'Accept-Encoding': 'none',
                       'Accept-Language': 'en-US,en;q=0.8',
                       'Connection': 'keep-alive'}
    # configure reuqest
    req = urllib2.Request(url,headers=hdr)
    # open the URL and get the response
    page = urllib2.urlopen(req)
    # load the JSON from the response
    data = json.load(page)
    #initialize data2 as a placeholder string
    data2 = 'null'
    # loop to compare the search query with all results
    for i in range(len(data)):
        title = data[i]['title']
        title = title.lower()
        if title in textCopy:
            data2 = data[i]['url']
            print '\nTitle : '+data[i]['title']
            print '\nArtist : '+data[i]['artist']['name']
            break
    if data2 == 'null':
        print '\nUnable to find the song'
    else:
        req = urllib2.Request(data2,headers=hdr)
        page = urllib2.urlopen(req)
        # get HTML contents of the lyrics page
        soup = BeautifulSoup(page)
        # get required lyrics
        data = soup.body.pre.string
        print '\n\n'+data
else:
    print 'No Internet connectivity. PLease check your network and try again'




