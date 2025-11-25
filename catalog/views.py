from django.shortcuts import render

def index(request):
    """Ana səhifə görünüşü"""
    return render(request, 'index.html')
