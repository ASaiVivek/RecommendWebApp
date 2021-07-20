from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User
import cv2
import shutil
import requests
#from .models import Music
import json
import datetime
import ujson
import orjson
import rapidjson
# Create your views here.

gemotion=''
state = False

def music(request):
    global gemotion

    x = datetime.datetime.now()
    print(x) 

    # with open('./mrecommend/media/mrecommend/music.JSON', 'r') as j:
    #     input_songs = json.loads(j.read())

    file = open('./mrecommend/media/mrecommend/music.JSON', 'r')
    input_songs = ujson.load(file)

    # with open('./mrecommend/media/mrecommend/music.JSON', 'r') as j:
    #     input_songs = orjson.loads(j.read())

    #with open('./mrecommend/media/mrecommend/music.JSON', 'r') as j:
     #   input_songs = rapidjson.loads(j.read())


    x=datetime.datetime.now()
    print(x)

    if gemotion == 'Sad':
        output_songs=[x for x in input_songs if x['genre'] == 'rock']
    elif gemotion == 'Happy':
        output_songs=[x for x in input_songs if x['genre'] == 'party']
    elif gemotion == 'Frustrated':
        output_songs=[x for x in input_songs if x['genre'] == 'pop']
    elif gemotion == 'Peaceful':
        output_songs=[x for x in input_songs if x['genre'] == 'pop']
    else:
        output_songs = input_songs

    x=datetime.datetime.now()
    print(x)                       

    return render(request, 'mrecommend/music.html',{
        "songs": output_songs
    })

def movies(request):
    global gemotion
    x = datetime.datetime.now()
    print(x)

    # with open('./mrecommend/media/mrecommend/movies.JSON', 'r') as j:
    #     input_movies = json.loads(j.read())
    
    file = open('./mrecommend/media/mrecommend/movies.JSON', 'r')
    input_movies = ujson.load(file)

    # with open('./mrecommend/media/mrecommend/movies.JSON', 'r') as j:
    #     input_movies = orjson.loads(j.read())

    #with open('./mrecommend/media/mrecommend/movies.JSON', 'r') as j:
     #   input_movies = rapidjson.loads(j.read())    

    x = datetime.datetime.now()
    print(x) 
    if gemotion == 'Sad': 
        output_movies=[x for x in input_movies if x['genre'] == 'party']
    elif gemotion == 'Happy':     
        output_movies=[x for x in input_movies if x['genre'] == 'thriller']
    elif gemotion == 'Frustrated':       
        output_movies=[x for x in input_movies if x['genre'] == 'smooth']
    elif gemotion == 'Peaceful':
        output_movies=[x for x in input_movies if x['genre'] == 'action']
    else:
        output_movies = input_movies                  
    x = datetime.datetime.now()
    print(x) 
    return render(request, 'mrecommend/movies.html',{
        "movies": output_movies
    })

def detectemotion(request):
    global gemotion
    global state
    url = "http://localhost:7000/emotion_detection/detect/"
    # image = cv2.imread("mrecommend/media/mrecommend/opencv0.png")
    payload = {"image": open("mrecommend/media/mrecommend/opencv0.png", "rb")}
    result = requests.post(url, files=payload).json()
    emotion = result["emotion"]
    if emotion == 'Fearful' or emotion == 'Sad':
        gemotion = 'Sad'
    elif emotion == 'Happy' or emotion == 'Surprised':
        gemotion = 'Happy'
    elif emotion == 'Angry' or emotion == 'Disgusted':
        gemotion = 'Frustrated'
    elif emotion == 'Neutral':
        gemotion = 'Peaceful'                 
      
    state = True
    return render(request, 'mrecommend/index.html',{
        "emotion" : gemotion,
        "state": state
    })



def imagecapture(request):
    cam = cv2.VideoCapture(0)

    for i in range(1):
        return_value, image = cam.read()
        cv2.imwrite('opencv'+str(i)+'.png', image)

    del(cam)

    og=r'opencv0.png'
    tg=r'mrecommend/media/mrecommend/opencv0.png'

    shutil.move(og,tg)

    return render(request, 'mrecommend/index.html')    
    
def index(request):
    global gemotion
    global state
    if request.user.is_authenticated:
        return render(request,"mrecommend/index.html",{
            "emotion": gemotion,
            "state" : state
        })
    else:
        return render(request, "mrecommend/login.html")


    

def logout_view(request):
    global gemotion
    global state
    state = False
    gemotion = ""
    logout(request)
    return HttpResponseRedirect(reverse("index"),{
        "emotion":gemotion,
        "state": False
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"),{
                "emotion": "",
                "state": False
            })
        else:
            return render(request, "mrecommend/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "mrecommend/login.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "mrecommend/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "mrecommend/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"),{
                "emotion": "",
                "state": False
            })
    else:
        return render(request, "mrecommend/register.html")
