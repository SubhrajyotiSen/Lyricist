import urllib2
from bs4 import BeautifulSoup

# the starting tag of the lyrics content
TEXT = ("<div>\n <!-- Usage of azlyrics.com content by any third-party lyrics provide"
        " is prohibited by our licensing agreement. Sorry about that. -->\n")
# HTML tags to be replaces in the lyrics result
replace_texts = ['\n <br>', '\n <br/>', '\n</div>', '\n <i>\n', '\n </i>', TEXT]

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
    	'Enter the artist name followed by the song or just the song name: \n')
    # convert input to lowercase for easy comparison
    textCopy = text.lower()
    # strip extra spaces
    text = text.strip()
    # format the string to a query
    text = text.replace(' ', '%20')
    # generate the API request URL
    url = 'http://search.azlyrics.com/search.php?q='+text
    soup = getSoup(url)
    # find divs with class 'panel'
    segments = soup.body.findAll("div", {"class": "panel"})
    # find the div that contains the song results
    for segment in segments:
        if segment.find("div", "panel-heading").find("b").text == "Song results:":
            link = segment.find("td", {"class": "text-left visitedlyr"}).find("a")['href']
    # if a song result is found
    if link is not None:
        soup = getSoup(link)
        # get the lyrics
        lyrics = soup.body.find(
            "div", {"class": "col-xs-12 col-lg-8 text-center"}).findAll("div")[6].prettify()
        # remove html tags from lyrics
        for text in replace_texts:
            lyrics = lyrics.replace(text, '')
        # print actual lyrics
        print lyrics
    else:
        print "Song not found"
else:
    print ('No Internet connectivity. '
           'PLease check your network and try again\n')
