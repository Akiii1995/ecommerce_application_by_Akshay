from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from .models import Profile

def login_page(request):
    # function for login user
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=email)

        if not user_obj.exists():
            messages.warning(request,'Account not found')
            return HttpResponseRedirect(request.path_info)

        if not user_obj[0].is_email_verfified:
            messages.warning(request,'Your account is not verified')
            return HttpResponseRedirect(request.path_info)

        user_obj = authenticate(username=email,password=password)
        if user_obj:
            login(request,user_obj)
            return redirect('/')
        messages.warning(request,'Invalid credentials')
        return HttpResponseRedirect(request.path_info)
    return render(request,'accounts/login.html')

def register_page(request):
    # function for signup user
    if request.method=='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=email)
        print(email, "email")
        if user_obj.exists():
            messages.warning(request,'Email is all ready taken.')
            return HttpResponseRedirect(request.path_info)
        user_obj = User.objects.create(first_name=first_name, last_name=last_name,email=email,username=email)
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request,'An Email has been sent on your mail')
        return HttpResponseRedirect(request.path_info)
    return render(request,'accounts/register.html')

def activate_email(request,email_token):
    try:
        user = Profile.objects.get(email_token=email_token)
        user.is_email_verified = True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponseRedirect(request.path_info)("Invalid Email Token")