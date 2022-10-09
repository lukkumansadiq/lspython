from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if cpassword == password:
            if User.objects.filter(username=username).exists():
                print('Username Already Taken, Try with Another Username')
                messages.info(request, 'Username Already Taken, Try with Another Username')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print('Email Already Taken, Try with Another Username')
                messages.info(request, 'Email Already Taken, Try with Another Email')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
                user.save()
                print('User Created')
                messages.info(request, 'Registration Successful!!')
                return redirect('login')

        else:
            print("Password Not Matches")
            messages.info(request, 'Password not Matching')
            return redirect('register')
        # return redirect('/')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:

            messages.info(request, 'Invalid Credentials')
            return redirect("login")
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
