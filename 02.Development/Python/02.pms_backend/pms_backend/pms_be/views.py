
from datetime import datetime
import glob
import os
from django.http import HttpResponse
from pms_be.models.e_employee import EEmployee

import requests
from bs4 import BeautifulSoup, Tag

def index( request):
    return HttpResponse("Hello World:")

def getCNN5():
 
    folder = "C:\\Users\\mtk26734\\Music\\"
    #folder = "C:\\Users\\mtk26734\\Desktop\\TEST\\"
    #1. Get link from CNN 5 things 
    r = requests.get("https://edition.cnn.com/audio/podcasts/5-things", verify=False)
    
    soup = BeautifulSoup(r.text, 'html.parser')
     
    f = open(folder+ "audio.txt", "w")
    for tag in  soup.find(id = "episodes").find_all("audio-player-wc"):
        t = Tag.__copy__(tag)
        link = t.attrs.get("src") + "\n"
        f.write(link)
        
    f.close()
    
    #2. remove files
    t = datetime.now().time()
    if t.hour < 9:
        if os.path.exists( folder) :
            files = glob.glob(folder + "*.mp3")
            for file in files:
                os.remove(file)

def test():
    folder = "C:\\Users\\mtk26734\\Desktop\\TEST\\"
    
    
    
    