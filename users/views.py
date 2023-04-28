from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile 
from .forms import CustomUserCreationForm

# Create your views here.

def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'username is not exist')

        user = authenticate(request, username=username,password=password)


        if user is not None:
            login(request,user)
            return redirect('profiles')
        else:
            messages.error(request,'Username or Password in incorrect')

    return render(request, 'users/login_register.html')

def logoutPage(request):
    logout(request)
    messages.info(request,'User was logout')
    return redirect('login')

def registerPage(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method =='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username= user.username.lower()
            user.save()

            messages.success(request,'USER IS SUCCESFULLY CREATED!')

            login(request,user)
            return redirect('profiles')
        else:
            messages.success(request,'Error Occured During Registration')


    context = {'page': page,'form':form}
    return render(request,'users/login_register.html',context)

def profiles(requset):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(requset,'users/profiles.html',context)


def userprofile(request,pk):
    profile = Profile.objects.get(id=pk)
    topskills = profile.skill_set.exclude(description__exact ="")
    otherskills = profile.skill_set.filter(description = "")

    context = {'profile': profile,'topskills': topskills, "otherskills": otherskills}
    return render(request,'users/user-profile.html',context)