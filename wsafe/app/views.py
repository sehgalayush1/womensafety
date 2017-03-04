from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def signup(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		username = request.POST['username']
		password = request.POST['password']
		verify_password = request.POST['verify_password']
		
		if password == verify_password:
			user = User.objects.create_user()
			user.username = username
			user.password = password
			user.email = email
			user.first_name = name
			user.save()
		
		else:
			error = 'The passwords you provided are not the same!'
			return render(request, 'signup.html', {'error':error})

		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect(reverse_lazy('dashboard'))
	
	return render(request, 'signup.html')



def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		
		if user is not None:
			login(request, user)
			return redirect(reverse_lazy('dashboard'))
	
	return render(request, 'index.html')



def logout_view(request):
	if not request.user.is_authenticated:
		return redirect(reverse_lazy('login'))

	logout(request)
	return redirect(reverse_lazy('login'))



def dashboard(request):
	return render(request, 'dashboard.html')
