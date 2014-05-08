""""
Reddit Wallpapers Script

Author: thebones2356
"""

import time
import praw

import datetime as dt
import imghdr
import urllib.request as urllib			
from PIL import Image
from io import BytesIO

r = praw.Reddit('r/wallpapers top crawler by u/thebones2356 v 1.0.'
                'Url: ')

#Check is it is an album
def isAlbum(url):
    if url.find("/a/") == -1:
        return False
    return True
    
#check is the site is imgur
def isImgur(url):
    if url.find("imgur") == -1:
        print("is not imgur so ignored")
        return False
    return True
    
if __name__ == '__main__':
    while True:
        #run this program forever! refreshes onve a day (86400 seconds)
        subreddit = r.get_subreddit('wallpapers')
        for submission in subreddit.get_top_from_day(limit=10):
            #Check if the link is NSFW
            if not submission.over_18:
                linkURL = submission.url
                if isImgur(linkURL) and not isAlbum(linkURL):
                    if linkURL[-4:-3] != '.':
                        linkURL = linkURL+".png"
                    img_file = urllib.urlopen(linkURL)
                    im_string = BytesIO(img_file.read())
                    try:
                        resized_image = Image.open(im_string)
                    except IOError:
                        print("Failed")
                        pass
                    saveFile = "{0}".format(dt.datetime.now().strftime("%Y-%m-%d %H-%M-%S"))
                    resized_image.save("C:\\Users\\Ben\\Desktop\\ImgurFiles\\"+saveFile+".png")
                else:
                    print("Is an Album so skip")
            # resized_image.save("C:\\Users\\Ben\\Desktop\\ImgurFiles\\{0}".format(str(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))),'png')
        time.sleep(86400)
