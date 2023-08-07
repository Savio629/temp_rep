from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import Doctor
from django.contrib import messages

# Create your views here.

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def navigation(request):
    return render(request,'navigationbar.html')

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'index.html')

def login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)

        try:
            if request.user:
                login(request,user)
                error = "No"

            else:
                error = "Yes"
                
        except Exception as e:
             error = "Yes"
             
            
            # return redirect('login')
    context = {'error':error}            
                # return redirect('login')
    return render(request,'login.html',context)

def logout_admin(request):
    error = ""
    logout(request)
    error = "Logouut Sucessfully"
    return redirect('login')

def view_doctor(request):
    doctor = Doctor.objects.all()
    context = {'doctor':doctor}
    return render(request,'doctor_view.html',context)

def add_doctor(request):
    error = ''
    if not request.user.is_authenticated:
        return redirect('login') 
    if request.method == 'POST':
        n = request.POST['name']   
        c = request.POST['contact']   
        sp = request.POST['special']
        try:
            Doctor.objects.create(name = n, mobile =c, special = sp) 
            error = 'No'
        except:
            error = 'Yes'
    else:
        pass
    d = {'error':error}
    return render(request, 'add_doctor.html',d)    


