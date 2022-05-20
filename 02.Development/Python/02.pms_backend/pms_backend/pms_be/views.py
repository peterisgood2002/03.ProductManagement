
from datetime import datetime
import glob
import os
from django.http import HttpResponse
from pms_be.models.e_employee import EEmployee

import requests
from bs4 import BeautifulSoup, Tag
import webbrowser
def index( request):
    return HttpResponse("Hello World:")

def getCNN5Things(request):
    result = getCNN5()
    return HttpResponse(result)
    
def getCNN5():
 
    folder = "C:\\Users\\mtk26734\\Music\\"
    #folder = "C:\\Users\\mtk26734\\Desktop\\TEST\\"
    #1. Get link from CNN 5 things 
    r = requests.get("https://edition.cnn.com/audio/podcasts/5-things", verify=False)
    
    soup = BeautifulSoup(r.text, 'html.parser')
     
    f = open(folder+ "audio.txt", "w")
    links = []
    for tag in  soup.find(id = "episodes").find_all("audio-player-wc"):
        t = Tag.__copy__(tag)
        link = t.attrs.get("src")
        links.append(link)
        
        f.write(link + "\n")
        
    f.close()
    
    #2. remove files
    t = datetime.now().time()
    if t.hour < 9:
        #2. remove files before 9:00
        if os.path.exists( folder) :
            files = glob.glob(folder + "*.mp3")
            for file in files:
                os.remove(file)
    
    result = "TEST <BR />" 
    #3. open website
    for i in [0, 1, 2]:
        html = '<a href={link} target="_blank"> {index} </a> <br />'
        result += html.format(link = links[i], index = i)
    
    return result

def test():
    
    
    
    
