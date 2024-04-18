from django.shortcuts import render,redirect
from app1.models import card


# Create your views here.
def home(request):
    return render(request,'home.html')
def dashboard(request):
    return render(request,'dashboard.html')
def add_card(request):
    return render(request,'add_card.html')
def add_card1(request):
    if request.method=='POST':
        name=request.POST['name'] 
        a=card(name=name)
        a.save()
    return redirect('add_card')
def view_card(request):
    a=card.objects.all().filter(status=0)
    return render(request,'view_card.html',{'a':a})
def Archeive(request,pk):
    a=card.objects.get(id=pk)
    print(a)
    a.status=1
    a.save()
    return redirect('view_card')
def view_Archeive(request):
    return render(request,'view_archeive.html')
