from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def dashboard(request):
    return render(request,'dashboard.html')
def add_cards(request):
    return render(request,'add_card.html')