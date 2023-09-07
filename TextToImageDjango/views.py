from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import openai, os, requests
from dotenv import load_dotenv
from django.core.files.base import ContentFile
from .models import TextToImage
api_key = ""
openai.api_key = api_key
def home(request):
    return render(request, "home.html")


def getAnswer(request):
    obj = None
    if api_key is not None:
        user_input = request.GET['question']
        response = openai.Image.create(
            prompt = user_input,
            size = '256x256'
        )
        
        img_url = response["data"][0]["url"]
        
        response = requests.get(img_url)
        
        img_file = ContentFile(response.content)

        count = TextToImage.objects.count() + 1
        fname = f"image-{count}.jpg"

        obj = TextToImage(query = user_input)
        obj.image.save(fname, img_file)
        obj.save()

        print("İŞTE OBJEM: " + obj.image.url)

        return render(request, 'home.html', {'obj': obj})
