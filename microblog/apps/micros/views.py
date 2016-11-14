from django.shortcuts import render
from .models import Blog, User

def index(request):
	context={
		"blogs": Blog.objects.all(),
		"users": User.objects.all()
	}
	return render(request,'micros/index.html', context)

def create_post(request):
	return redirect(request, 'micros/create_post')

# Create your views here.
