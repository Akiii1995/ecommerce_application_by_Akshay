from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

def login_page(request):
    return render(request,'accounts/login.html')

def register_page(request):
    # function for signup user
    if request.method=='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=email)
        if user_obj.exists():
            messages.warning(request,'Email is all ready taken.')
            return HttpResponseRedirect(request.path_info)
        user_obj = User.objects.create(first_name=first_name, last_name=last_name,email=email,username=email)
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request,'An Email has been sent on your mail')
        return HttpResponseRedirect(request.path_info)
    return render(request,'accounts/register.html')