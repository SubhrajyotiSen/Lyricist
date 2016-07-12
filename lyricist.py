import urllib2
import json
from BeautifulSoup import BeautifulSoup

def connected(host='http://google.com'):
    try:
        urllib2.urlopen(host)
        return True
    except:
        return False
if connected():
    text = raw_input('Enter the artist name followed by the song or just the song name: \n')
    textCopy = text.lower()
    text = text.strip();
    text = text.replace(' ','%20')
    url = 'http://api.lyricsnmusic.com/songs?api_key=49dfa11af9c2fc5aa0085766477519&q='+text
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                       'Accept-Encoding': 'none',
                       'Accept-Language': 'en-US,en;q=0.8',
                       'Connection': 'keep-alive'}
    req = urllib2.Request(url,headers=hdr)
    page = urllib2.urlopen(req)
    data = json.load(page)
    data2 = 'null'
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
    soup = BeautifulSoup(page)
    data = soup.body.pre.string
    print '\n\n'+data
else:
    print 'No Internet connectivity. PLease check your network and try again'




