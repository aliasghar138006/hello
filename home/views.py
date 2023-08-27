from django.shortcuts import render
from .models import HomeModel

# Create your views here.


def HomePageView(request):
    Model = HomeModel.objects.all()
    print(Model[0])
    return render(request , 'index.html' , {'name' : Model[0]})
