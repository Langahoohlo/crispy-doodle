from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import User


# Example registration
def register_user(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']

    user = User.objects.create_user(username=username, email=email, password=password)
    user.save()


# Example login
def login_user(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        # Redirect or perform further actions
    else:
        print("Invalid username or password")
        # Handle login failure


def display_user_info(request):
    user = request.user
    print(f"Username: {user.username}")
    print(f"Email: {user.email}")
    print(f"First Name: {user.first_name}")
    print(f"Last Name: {user.last_name}")
