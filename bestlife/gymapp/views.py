from django.shortcuts import render,redirect

# Create your views here.

def home(request):
    return redirect('/index')

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def trainer(request):
    return render(request,'trainer.html')

def why(request):
    return render(request,'why.html')

def login(request):
    return render(request,'login.html')