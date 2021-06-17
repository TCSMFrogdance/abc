from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'home.html')

def About(request):
    return render(request, 'about.html')

def Story(request):
    return render(request, 'story.html')