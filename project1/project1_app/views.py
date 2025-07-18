from django.shortcuts import render

# Create your views here.
from .models import *
import json
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from django.db.models import Count
import re
import os
from django.views.decorators.cache import never_cache
from django.core.files.storage import FileSystemStorage
from datetime import date
from datetime import datetime


# Create your views here.

@never_cache
def show_index(request):
    return render(request, "index.html", {})


@never_cache
def logout(request):
    if 'uid' in request.session:
        del request.session['uid']
    return render(request,'index.html')

def register(request):
	username=request.POST.get("username")
	password=request.POST.get("password")
	mobile=request.POST.get("mobile")
	p_address=request.POST.get("p_address")

	print(username,password,user_type,mobile,p_address)


	obj10=Requests.objects.filter(mobile=mobile,username=username,password=password,p_address=p_address,user_type=user_type)
	co=obj10.count()
	if co==1:
		return HttpResponse("<script>alert('Request is in Pending list');window.location.href='/show_index/'</script>")

	else:
		obj1=Requests(mobile=mobile,username=username,password=password,p_address=p_address,user_type=user_type)
		obj1.save()
		return HttpResponse("<script>alert('Request sent, Wait For Approval');window.location.href='/show_index/'</script>")




def check_login(request):
	username = request.POST.get("username")
	password = request.POST.get("password")

	print(username)
	print(password)

	if username == 'admin' and password == 'admin':
		request.session["uid"] = "admin"
		return HttpResponse("<script>alert('Admin Login Successful');window.location.href='/show_home_admin/'</script>")
	
	else:
		
		obj2=Users.objects.filter(username=username,password=password)
		c2=obj2.count()
		if c2==1:
			ob9=Users.objects.get(username=username,password=password)
			request.session["uid"] = ob9.u_id
			request.session["username"]=ob9.username
			return HttpResponse("<script>alert('User Login Successful');window.location.href='/show_home_user/'</script>")
		else:
			return HttpResponse("<script>alert('Invalid');window.location.href='/show_index/'</script>")


@never_cache
###############ADMIN START
def show_home_admin(request):
	if 'uid' in request.session:
		print(request.session['uid'])
		return render(request,'home_admin.html') 
	else:
		return render(request,'index.html')
