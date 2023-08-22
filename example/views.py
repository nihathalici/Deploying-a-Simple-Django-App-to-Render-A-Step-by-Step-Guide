from django.shortcuts import render

def mainView(request):
    return render(request, "index.html")
