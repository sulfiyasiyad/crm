from django.shortcuts import render,redirect
from app1.models import card


# Create your views here.
def home(request):
    return render(request,'home.html')
def dashboard(request):
    return render(request,'dashboard.html')
def add_card(request):
    return render(request,'add_card.html')

def view_Archeive(request):
    return render(request,'view_archeive.html')
