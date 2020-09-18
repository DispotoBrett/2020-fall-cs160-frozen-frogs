from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    return HttpResponse("<h1>Frozen Frogs 🐸🐸🐸🐸🐸🐸🐸🐸🐸</h1><br>Time:{0}".format(datetime.now()))

def profile(request):
	return HttpResponse("<h2>Profile Page</h2>")
