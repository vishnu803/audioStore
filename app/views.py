from django.shortcuts import render
import uuid
from django.http import HttpResponse
from .models import *
from django.contrib import messages
# import pygeoip
# from django.contrib.gis.geoip2 import GeoIP2

# Create your views here.

def upload(request):
    if(request.method=='GET') :
        return render(request, 'upload.html')
    elif(request.method=='POST'):
        audio_file = request.FILES['audio']
        audioobj = audioStore(file = audio_file)
        audioobj.save()
        li=audioStore.objects.all()
        for k in li:
            print(k.uploaded_at)
        messages.info(request, 'Your file is succesfully uploaded')
        return render(request, 'upload.html')

def viewuploaded(request):
    records = audioStore.objects.all()
    return render(request, 'viewuploaded.html', {'records' : records})

