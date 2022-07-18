from django.shortcuts import render
from django.http import HttpResponse
from .models import  Contact,Commet
#from website.forms import connectform,commentform
from django.http import HttpResponseRedirect
from django.contrib import messages


# Create your views here.


def index(request):
    return render(request, "index.html")

def about(request):
    return render(request,"about.html")

def course(request):
    return render(request, "course.html")

def blog(request):
    if request.method=="POST":
        obj=Commet(name=request.POST["name"],email=request.POST["email"],
                   message=request.POST["message"])
        obj.save()
        messages.success(request,'Data  Was Be Sucessfully submited ')
        return HttpResponseRedirect('/blogpage')

    return render(request,'blog.html')

def blogpage(request):
    return render(request, 'blog.html')

def contact(request):
    if request.method=="POST":
        obj=Contact(name=request.POST["name"],email=request.POST["email"],
                    subject=request.POST["subject"],
                    message=request.POST["message"])
        obj.save()
        messages.success(request,'Data  Was Be Sucessfully submited ')
        return HttpResponseRedirect('/submit')
    return render(request,'contact.html')

def submit(request):
    return render(request,"contact.html")
