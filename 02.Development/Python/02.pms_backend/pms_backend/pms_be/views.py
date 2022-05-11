
from django.http import HttpResponse
from pms_be.models.e_employee import EEmployee

import requests
from bs4 import BeautifulSoup, Tag

def index( request):
    return HttpResponse("Hello World:")

def getCNN5():
     #e = EEmployee( id = 1, english_name = "test")
     #e.save()
     
    r = requests.get("https://edition.cnn.com/audio/podcasts/5-things", verify=False)
    
    soup = BeautifulSoup(r.text, 'html.parser')
     
    f = open("C:\\Users\\mtk26734\\Desktop\\audio.txt", "w")
    for tag in  soup.find(id = "episodes").find_all("audio-player-wc"):
        t = Tag.__copy__(tag)
        link = t.attrs.get("src") + "\n"
        f.write(link)
        
    f.close()
    
    
    
    