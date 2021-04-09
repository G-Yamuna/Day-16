from django.shortcuts import render,redirect
from NoteApp.forms import UsForm
# Create your views here.

def home(r):
	return render(r,'stc/home.html')

def aboutus(r):
	return render(r,'stc/aboutus.html')

def contactus(r):
	return render(r,'stc/contactus.html')

def regi(r):
	if r.method=="POST":
		p=UsForm(r.POST)
		if p.is_valid():
			p.save()
			return redirect('/lg')
	p=UsForm()
	return render(r,'stc/register.html',{'u':p})

def dashboard(re):
	return render(re,'stc/dashboard.html')