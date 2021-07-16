from django.shortcuts import render
from .models import Video

def test_page(request):
    video=Video.objects.all()
    return render(request,'intranet/test.html',{'video':video})

def main_page(request):
    return render(request,'intranet/main.html',{})
# Create your views here.
