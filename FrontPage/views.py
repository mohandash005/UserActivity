from django.shortcuts import HttpResponse, render, get_object_or_404, redirect
from django.contrib import messages
from . models import User, User_Activity
from django.contrib.auth import hashers
from passlib.hash import django_pbkdf2_sha256
import json
import requests
from django.core import serializers
import datetime

Dat = datetime.datetime.now()
fullname = ""
def Login(request):
    if request.method == 'POST':
        mail = request.POST.get('email')
        passwd = request.POST.get('password')
        if mail == "":
            messages.info(request,'Please fillup all fields')
            return redirect('/Login')
        else:
            data = User.objects.all().filter(Mail=mail)
            check=serializers.serialize('json', data)                #query to json data conversation
            dta=check
            dt= json.loads(dta)                                      #converts string to list
            name= dt[0]['fields']['FullName']
            check = django_pbkdf2_sha256.verify(passwd, dt[0]['fields']['Password'])
            if User.objects.filter(Mail=mail) and check == True:
                globals()['Dat'] = datetime.datetime.now()
                globals()['fullname'] = name
                return render(request,'Home.html',{'name':name})
            else:
                messages.info(request,'Please Incorrect Data')
                return redirect('/Login')
    return render(request,'Login_Page.html',{})

def Signup(request):
    if request.method == 'POST':
        name = request.POST.get("Name")
        email= request.POST.get("Email")
        createPassword= request.POST.get("CreatePassword")
        confirmPassword= request.POST.get("ConfirmPassword")
        if name == "" or email == "" or createPassword == "" or confirmPassword == "":
            messages.info(request,'Please fillup all fields')
            return redirect('/Sign')
        else:
            if createPassword == confirmPassword:
                if User.objects.filter(Mail=email):
                   messages.info(request,'Email Already used')
                   return redirect('/Sign')
                else:
                    response = requests.get("http://ip-api.com/json")
                    todos = json.loads(response.text)
                    location= todos['country'] + "/" + (todos['city'])
                    print(location)
                    new_password = hashers.make_password(createPassword)
                    print(new_password)
                    user = User(FullName=name,Mail=email,Location=location,Password=new_password)
                    user.save()
                    print('User created')
                    messages.info(request,'User Created')
                    return redirect('/Login')
            else:
                messages.info(request,'Password not matching')
                return redirect('/Sign')
    else:
        return render(request, 'Signup.html',{})


def Logout(request):
    StartTime = Dat
    EndTime = datetime.datetime.now()
    name = fullname
    response = requests.get("http://ip-api.com/json")
    todos = json.loads(response.text)
    location= todos['country'] + "/" + (todos['city'])
    print(location)
    print(name)
    print(StartTime)
    print(EndTime)
    if StartTime and EndTime and location and name:
        user_activity = User_Activity(FullName=name,location=location,start_time=StartTime,end_time=EndTime)
        user_activity.save()
        return render(request,'Logout.html')
    else:
        print("Something went wrong")
        return redirect('/Login')
