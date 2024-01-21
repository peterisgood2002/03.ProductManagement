from datetime import datetime
import glob
import os
from django.http import HttpResponse
from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup, Tag
import webbrowser
from pathlib import Path
from pms_dbmodel.project import ProjectService
from pms_dbmodel.testprojectdata import TestProjectData
from pms_platform.services import PlatformService
from pms_project.services import ProjectService as ps
from pms_milestone.services import MilestoneService


def index(request):
    return HttpResponse("Hello World:")


def getCNN5Things(request):
    result = getCNN5()
    return HttpResponse(result)


def getCNN5():
    folder = "output"
    # folder = "C:\\Users\\mtk26734\\Desktop\\TEST\\"
    # 1. Get link from CNN 5 things
    r = requests.get("https://edition.cnn.com/audio/podcasts/5-things", verify=False)

    soup = BeautifulSoup(r.text, "html.parser")

    f = open(folder + "audio.txt", "w")
    links = []
    for tag in soup.find(id="episodes").find_all("audio-player-wc"):
        t = Tag.__copy__(tag)
        link = t.attrs.get("src")
        links.append(link)

        f.write(link + "\n")

    f.close()

    # 2. remove files
    t = datetime.now().time()
    if t.hour < 9:
        # 2. remove files before 9:00
        if os.path.exists(folder):
            files = glob.glob(folder + "*.mp3")
            for file in files:
                os.remove(file)

    result = "TEST <BR />"
    # 3. open website
    for i in [0, 1, 2]:
        html = '<a href={link} target="_blank"> {index} </a> <br />'
        result += html.format(link=links[i], index=i)

    return result


def testDB(request):
    project = TestProjectData.getProject1()

    ProjectService.addProject(project)
    return HttpResponse("TEST")


def addPlatform(request):
    path_home = str(Path(__file__).parents[1])
    print("PATH = " + path_home)
    fileName = path_home + "./pms_platform/input_test/test.xlsx"
    PlatformService.parse(fileName)

    return HttpResponse("addPlatform")


def addProject(request):
    path_home = str(Path(__file__).parents[1])
    print("PATH = " + path_home)
    fileName = path_home + "./pms_project/input_test/test.xlsx"
    ps.parse(fileName)

    return HttpResponse("addProject")


def addMilestone(request):
    path_home = str(Path(__file__).parents[1])
    print("PATH = " + path_home)
    fileName = path_home + "./pms_milestone/input_test/test.xlsx"
    MilestoneService.parse(fileName)

    return HttpResponse("addMilestone")


def addCustomer(request):
    return HttpResponse("TEST")
