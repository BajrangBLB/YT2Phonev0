from django.shortcuts import render, HttpResponse
from .models import Contact
from django.contrib import messages
import pytube
from pytube import YouTube
import os
import io
import random

# Create your views here.



def index(request):
    return render(request, 'index.html')


def download_video(request):
    return render(request, 'download_video.html')


def download_audio(request):
    return render(request, 'download_audio.html')


def privacy_policy(request):
    return render(request, 'privacy_policy.html')


def contact_us(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        contact = Contact(name=name, email=email, message=message)
        contact.save()

        messages.success(request, 'Your message is sent.')

    return render(request, 'contact_us.html')


def test_mp3(request):
    link = request.GET.get("link")

    try:
        yt = YouTube(link)
        return download_test_mp3(link)

    except Exception as e:
        messages.error(request, 'Please enter a valid url or try to reload.')
        return render(request, "download_audio.html")


def test_360(request):
    link = request.GET.get("link")

    try:
        yt = YouTube(link)
        return download_360(link)

    except Exception as e:
        messages.error(request, 'Please enter a valid url or try to reload.')
        return render(request, "download_video.html")


def test_720(request):
    link = request.GET.get("link")

    try:
        yt = YouTube(link)
        return download_720(link)


    except Exception as e:
        messages.error(request, 'Please enter a valid url or try to reload.')
        return render(request, "download_video.html")


def download_720(link):
    number = random.randint(1, 1000)

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    filename = f'video_720_{number}.mp4'
    yt = YouTube(link)

    yt.streams.filter(res="720p", progressive=True).first().download(BASE_DIR)
    os.rename(yt.streams.filter(res="720p", progressive=True).first().default_filename, filename)

    with open(os.path.join(BASE_DIR, filename), 'rb') as f:
        data = f.read()

    print("Download complete... {}".format(filename))

    response = HttpResponse(data, content_type='video/mp4')
    response['Content-Disposition'] = f'attachment; {filename}'
    os.remove(os.path.join(BASE_DIR, filename))
    return response


def download_360(link):
    number = random.randint(1, 1000)

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    filename = f'video_360_{number}.mp4'
    yt = YouTube(link)

    yt.streams.filter(res="360p", progressive=True).first().download(BASE_DIR)
    os.rename(yt.streams.filter(res="360p", progressive=True).first().default_filename, filename)

    with open(os.path.join(BASE_DIR, filename), 'rb') as f:
        data = f.read()

    print("Download complete... {}".format(filename))

    response = HttpResponse(data, content_type='video/mp4')
    response['Content-Disposition'] = f'attachment; {filename}'
    os.remove(os.path.join(BASE_DIR, filename))
    return response


def download_test_mp3(link):
    number = random.randint(1, 1000)

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    filename = f'audio{number}.mp3'
    yt = YouTube(link)

    yt.streams.filter(only_audio=True).first().download(BASE_DIR)
    os.rename(yt.streams.filter(only_audio=True).first().default_filename, filename)

    with open(os.path.join(BASE_DIR, filename), 'rb') as f:
        data = f.read()

    print("Download complete... {}".format(filename))

    response = HttpResponse(data, content_type='audio/mpeg')
    response['Content-Disposition'] = f'attachment; {filename}'
    os.remove(os.path.join(BASE_DIR, filename))
    return response
