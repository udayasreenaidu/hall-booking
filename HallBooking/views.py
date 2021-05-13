from django.shortcuts import render,redirect
from . forms import Usrg,UpdaPfl,Im
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
import secrets

# Create your views here.

def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def search(request):
	return render(request,'html/search.html')

def contact(request):
	return render(request,'html/contact.html')



def register(request):
	if request.method == "POST":
		p = Usrg(request.POST)
		if p.is_valid():
			p.save()
			messages.success(request,"You have successfully registered")
			return redirect('/login')
	p = Usrg()
	return render(request,'html/register.html',{'k':p})

@login_required
def dashboard(request):
	z = CrNt.objects.filter(crt_id=request.user.id).count()
	d = "{:02}".format(z)
	k = CrNt.objects.all()
	zy = []
	for h in k:
		zy.append(h.id)
		pass
	ss = zy[-1]-int(d)
	ss = "{:02}".format(ss)
	return render(request,'html/dashboard.html',{'cr':d,'dl':ss})

@login_required
def prfle(request):
	return render(request,'html/profile.html')

def updfple(request):
	if request.method == "POST":
		m = UpdaPfl(request.POST,instance=request.user)
		n = Im(request.POST,request.FILES,instance=request.user.updf)
		if m.is_valid() and n.is_valid():
			m.save()
			n.save()
			messages.success(request,"Profile updated Successfully")
			return redirect('/pfle')
	m = UpdaPfl(instance=request.user)
	n = Im(instance=request.user.updf)
	return render(request,'html/updateprofile.html',{'p':m,'r':n})

@login_required
def booknow(request):
	return render(request,'html/booking.html')





