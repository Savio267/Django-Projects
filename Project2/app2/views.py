from django.shortcuts import render

def register(request):
    return render(request,'register.html')

def user_login(request):
    return render(request,'user_login.html')

def user_logout(request):
    return render(request,'user_logout.html')
