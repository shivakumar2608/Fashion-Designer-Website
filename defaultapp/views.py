from email import message
from webbrowser import get
from django.shortcuts import redirect, render , HttpResponse
from datetime import datetime
from defaultapp import models
from defaultapp.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    content = {
        "namee" : "Shiva"
    }
    return render(request, 'index.html', content)

def about(request):
    return render(request, 'aboutus.html')
def services(request):
    return HttpResponse("This is services page")
def contact(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        reason = request.POST.get('reason')
        contact = Contact(firstname=firstname, lastname=lastname,  email= email, phone= phone,reason = reason, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent, We will contact you soon..!')

    return render(request, 'contact.html')
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username= username, password = password)
        if user is not None:
        # A backend authenticated the credential    
            auth.login(request, user)
            messages.success(request, "Logged in")
            return redirect('/')
        else:
        # No backend authenticated the credentials
            messages.error(request, "Bad Credentials")
            print("hiiii")
            return redirect('/signin')
    else:        
        return render(request, 'signin.html')

def maggamblouses(request):
    return render(request, 'maggamblouses.html')
def designblouses(request):
    return render(request, 'designblouses.html')
def signup(request):
    if request.method =="POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if(pass1==pass2):
            if(User.objects.filter(username=username).exists()):
                messages.error(request, "Username already taken, Choose another")
            elif(User.objects.filter(email=email).exists()):
                messages.error(request, "Email already exsist, Choose another")
            else:
                user = User.objects.create_user(username,email,  pass1 )
                user.save()
                messages.success(request, "You have been created successfully")    
                return redirect("signin")
        else:
            messages.error(request, "Password doesn't match, Try Again");    
    return render(request, 'signup.html')    



