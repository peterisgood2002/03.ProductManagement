
from datetime import datetime
import glob
import os
import certifi
from django.http import HttpResponse
from pms_be.models.e_employee import EEmployee
from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup, Tag
import webbrowser
def index( request):
    return HttpResponse("Hello World:")

def getCNN5Things(request):
    getCNN5()
    return HttpResponse("Hello World:")
    
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
        
        #3. open website
        for i in [0, 1, 2]:
            webbrowser.open(links[i])

def testCRREST():
    certifi.where()
    folder = "C:\\Users\\mtk26734\\Desktop\\TEST\\"
    
    url = "http://172.21.101.232/secweb-web-script/mtk/mtkScriptLogin.action?"
    
    data = {
        "method":"login",
        "repository": "DigitHome",
        "userDb": "AUTO",
        "password": "U0654t/6",
        "loginId" : "MTK26734"
    }
    data = urlencode(data)
    resp = requests.get(url+data)
    #resp = requests.post(url, data = data)

    output = open(folder + 'test.xls', 'wb')
    output.write(resp.content)
    output.close()
    
    