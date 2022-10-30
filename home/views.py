from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'home_index.html')


def video(request):
    return render(request, 'index.html')


def intro(request):
    return render(request, 'intro.html')
