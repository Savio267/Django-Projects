from django.shortcuts import render
from app1.models import Book
from app1.models import Person
from app1.models import Myuser
from app1.forms import bookform
from app1.forms import personform
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages


def home(request):
    return render(request,'home.html')

def fact(request):
    if(request.method=="POST"):
        n=int(request.POST['n'])
        f=1
        for i in range(1,n):
            f=f*i
            return render(request,'fact.html',{'f':f})
    return render(request,'fact.html')

def addbook(request):
    if(request.method=="POST"):
        t=request.POST['t']
        a=request.POST['a']
        p=request.POST['p']
        f=request.FILES['f']
        i=request.FILES['i']
        b=Book.objects.create(title=t,author=a,price=p,pdf=f,cover=i)
        b.save()
        return viewbook(request)
    return render(request,'addbook.html')

def addbook1(request):
    f=bookform()
    if(request.method=="POST"):
        f=bookform(request.POST)
        if f.is_valid():
            f.save()
            return viewbook(request)
    return render(request,'addbook1.html',{'f':f})

def addpersons(request):
    if(request.method=="POST"):
        n=request.POST['n']
        p=request.POST['p']
        a=request.POST['a']
        b=Person.objects.create(name=n,place=p,age=a)
        b.save()
        return viewpersons(request)
    return render(request,'addpersons.html')

def addpersons1(request):
    f=personform()
    if(request.method=="POST"):
        f=personform(request.POST)
        if f.is_valid():
         f.save()
         return viewpersons(request)
    return render(request,'addpersons1.html',{'f':f})

def viewbook(request):
    k=Book.objects.all()
    return render(request,'viewbook.html',{'b':k})


def viewpersons(request):
     k=Person.objects.all()
     return render(request,'viewpersons.html',{'b':k})

def view_book(request,p):
    b=Book.objects.get(id=p)
    return render(request,'viewbook.html',{'b':b})

def delete_book(request,p):
    b=Book.objects.get(id=p)
    b.delete()
    return viewbook(request)

def edit_book(request,p):
    b=Book.objects.get(id=p)
    f=bookform(instance=b)
    if(request.method=="POST"):
        f=bookform(request.POST,request.FILES,instance=b)
        if f.is_valid():
            f.save()
            return viewbook(request)
    return render(request,'addbook1.html',{'f':f})


def register(request):
    if (request.method=="POST"):
        u=request.POST['u']
        f=request.POST['f']
        l=request.POST['l']
        e=request.POST['e']
        p=request.POST['p']
        s=request.POST['s']
        n=request.POST['n']
        u=Myuser.objects.create_user(username=u,first_name=f,last_name=l,email=e,password=p,place=s,phone=n)
        u.save()
    return render(request,'register.html')

def admin_signup(request):
    if (request.method=="POST"):
        u=request.POST['u']
        f=request.POST['f']
        l=request.POST['l']
        e=request.POST['e']
        p=request.POST['p']
        s=request.POST['s']
        n=request.POST['n']
        u=Myuser.objects.create_user(username=u,first_name=f,last_name=l,email=e,password=p,place=s,phone=n)
        u.is_admin=True
        u.save()
        return home(request)
    return render(request,'adminsignup.html')


def teacher_signup(request):
    if (request.method=="POST"):
        u=request.POST['u']
        f=request.POST['f']
        l=request.POST['l']
        e=request.POST['e']
        p=request.POST['p']
        s=request.POST['s']
        n=request.POST['n']
        u=Myuser.objects.create_user(username=u,first_name=f,last_name=l,email=e,password=p,place=s,phone=n)
        u.is_teacher=True
        u.save()
        return home(request)
    return render(request,'teachersignup.html')


def person_signup(request):
    if (request.method=="POST"):
        u=request.POST['u']
        f=request.POST['f']
        l=request.POST['l']
        e=request.POST['e']
        p=request.POST['p']
        s=request.POST['s']
        n=request.POST['n']
        u=Myuser.objects.create_user(username=u,first_name=f,last_name=l,email=e,password=p,place=s,phone=n)
        u.is_person=True
        u.save()
        return home(request)
    return render(request,'personsignup.html')


def user_login(request):
     if(request.method=="POST"):
       u = request.POST['u']
       p = request.POST['p']
       user=authenticate(username=u,password=p)
       if (user and user.is_admin==True):
           login(request,user)
           return render(request,'adminhome.html')
       elif (user and user.is_teacher==True):
           login(request,user)
           return render(request,'teacherhome.html')
       elif (user and user.is_person==True):
           login(request,user)
           return render(request,'personhome.html')
       else:
        messages.error(request,"INVALID CREDENTIALS")
     return render(request,'user_login.html')

def user_logout(request):
        logout(request)
        return user_login(request)


