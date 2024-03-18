from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from . models import Profile
# from credentials.models import CustomUser
from django.contrib.auth.models import AbstractUser


# Create your views here.

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return  redirect('/')
        else:
            messages.info(request,"Invalid username or password")
            return redirect('login')
    return render(request,'login.html')

def registration(request):
    if request.method == 'POST':
        username=request.POST['username']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['c_password']
        # profile_img = request.POST['profile_img']
        # dob = request.POST['dob']
        if password == c_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exist")
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"E-mail already exist")
                return redirect('registration')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save();
                messages.success(request, 'Registration successful! You can now log in.')
                return redirect('login')

        else:
            messages.info(request,"password not matching")
            return redirect('registration')
        return redirect('/')

    return render(request,"registration.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def myprofile(request):
    user = request.user

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            # messages.success(request, 'Profile updated successfully!')
            return redirect('/')
        else:
            messages.error(request, 'Error updating profile. Please check the form.')

    else:
        form = UserProfileForm(instance=user)

    return render(request, 'myprofile.html', {'form': form})

# def update(request,id):
#     movie=Movie.objects.get(id=id)
#     forms=MovieForm(request.POST or None,request.FILES,instance=movie)
#     if forms.is_valid():
#         forms.save()
#         return redirect('/')
#     return render(request,'edit.html',{'form':forms,'movie':movie})