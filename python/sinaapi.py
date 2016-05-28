"https://api.weibo.com/2/place/pois/photos.json"

accessToken = "2.00juYUmF0dYhVk4f50df99a8UEKkD"
poiid = "82094757DA6EA4FD4092"
count = "50"
page = "1"
url = baseUrl + "?" + "access_token=" + accessToken + "&poiid="
+ poiid + "&count=" + count + "&page=" + page


import urllib2
import json
import time
import math

def fetch(url):
    response = urllib2.urlopen(url)
    data = response.read()
    parsedData = json.loads(data)
    
    time.sleep(1)
    
    return parsedData

parsedData = fetch(url)

numPosts = parsedData["total_number"]

numPages = int(math.ceiling( float(numPosts) / float(count) ))

print "total number of pages: " ,str(numPages)


for i in range(numPages):
    page = str(i + 1)
    url = baseUrl + "?" + "access_token=" + accessToken + "&poiid=" + poiid + "&count=" + count + "&page=" + page
    parsedData = fetch(url)
    posts = parsedData["statuses"]

    print len(posts)
    
    for post in posts:
        try:
            uid = post["user"]["id"]
        except:
            print "user id error!"
            uid = " " 
               
        print uid 
    
    print "-----"
    print "finished page " + page