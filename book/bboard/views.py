from .models import Bb
from django.shortcuts import render
 
def index(request):
    bbs = Bb.objects.all()
    