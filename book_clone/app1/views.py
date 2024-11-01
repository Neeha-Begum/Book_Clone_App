from django.shortcuts import render,redirect
from app1.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='loginpage')
def homeview(request):
    obj=Book.objects.all()[::-1]
    if request.method=="POST":
        a=request.POST.get('search')
        result=Book.objects.filter(title__icontains=a)
        return render(request,'home.html',{'books':result})
    return render(request,'home.html',{'books':obj})

def loginview(request):
    if request.method=="POST":
        a=request.POST.get('uname')
        b=request.POST.get('passw')
        if User.objects.filter(username=a).exists():
            obj=User.objects.get(username=a)
            login(request,obj)
            if request.user.is_superuser:
                return redirect('/admin')
            else:
                return redirect('homepage')
    return render(request,'login.html')

def registerview(request):
    if request.method=="POST":
        a=request.POST.get('usern')
        b=request.POST.get('email')
        c=request.POST.get('passw')
        d=request.POST.get('cpass')

        if User.objects.filter(username=a).exists():
            return redirect('loginpage')
        
        if len(c)<8:
            return redirect('registerpage')
        
        if c==d:
            obj=User(username=a,email=b)
            obj.set_password(c)
            obj.save()
            return redirect('loginpage')
        else:
            return redirect('registerpage')
        
    return render(request,'register.html')


def bookview(request):
    objs=Author.objects.all()
    if request.method=="POST":
        a=request.POST.get('author')
        b=request.POST.get('title')
        c=request.FILES.get('image')
        d=request.FILES.get('files')
        e=request.POST.get('genre')
        f=int(request.POST.get('price'))
        obj=Author.objects.get(name=a)
        objs=Book(title=b,image=c,file=d,genre=e,price=f,author=obj)
        objs.save()
        return redirect('homepage')
    return render(request,'book.html',{'res':objs})

def authorview(request):
    if request.method=="POST":
        a=request.POST.get('aname')
        b=request.POST.get('published_year')
        c=request.POST.get('nationality')
        obj=Author(name=a,published_year=b,nationality=c)
        obj.save()
        if request.user.is_staff:
            return redirect('bookpage')
        else:
            return redirect('homepage')
    return render(request,'author.html')

def deleteview(request,rid):
    if request.user.is_staff:
        obj=Book.objects.get(id=rid)
        obj.delete()
    return redirect('homepage')


def updateview(request,rid):
    obj=Book.objects.get(id=rid)
    
    if request.user.is_staff:
        if request.method=="POST":
            a=request.POST.get('author')
            b=request.POST.get('title')
            c=request.FILES.get('image')
            d=request.FILES.get('files')
            e=request.POST.get('genre')
            f=int(request.POST.get('price'))
            g=int(request.POST.get('published_year'))

            author,created=Author.objects.get_or_create(name=a)
            if c:
                obj.author=author
                obj.published_year=g
                obj.title=b
                obj.image=c
                obj.genre=e
                obj.price=f
                obj.save()
            else:
                obj.file=d
                obj.author=author
                obj.author=g
                obj.title=b
                obj.genre=e
                obj.price=f
                obj.save()
            return redirect('homepage')
        return render(request,'update.html',{'res':obj})
    return render(request,'update.html')


def dedicatedview(request,rid):
    if Book.objects.filter(id=rid).exists():
        a=Book.objects.get(id=rid)
        return render(request,'dedicated.html',{'result':a})
    else:
        return redirect('homepage')

def logoutview(request):
    logout(request)
    return redirect('loginpage')