from django.shortcuts import render
from auth_user_app.forms import UserForm, UserProfileInfoForm

#
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'auth_user_app/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index')) # redirect to index after logout

def register(request):
    
    # we assumed user not registered yet
    registered = False # tell if someone is registered or not
    
    # if request is POST then grab info from form
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            
            user = user_form.save() #  save USER form to db, (user_form from forms.py UserForm class)
            user.set_password(user.password) # hash password .set_password() then
            user.save()  # save hashed password to db
            
            # extra information
            profile = profile_form.save(commit=False) # commit=False : dont save to db yet
            profile.user = user 
            # link one to one relationship with user_form = UserForm(data=request.POST) which come from forms.py UserForm model = User
            # it kinda create one to one relationship between User from django database and UserProfileInfo as extra attributes
            
            # check if they provided PP
            if 'profile_pic' in request.FILES: # FILES is used for file upload
                profile.profile_pic = request.FILES['profile_pic'] # kinda like Dict : 'profile_pic'
            
            # save the model
            profile.save()
            
            # then register
            registered = True
        else:
            print(user_form.errors, profile_form.errors) # tuppples
    
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    
    
    return render(request, 'auth_user_app/registration.html', 
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}) # for registration.html for context




# login section

def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user: # pass the auth 
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index')) # response redirect to index after login
            else:
                return HttpResponse("Your account is disabled/ not active") # if user is not active
        else:
            print("someone tried to login and failed")
            print(f"Username{username} and password {password}")
            return HttpResponse("Invalid login details supplied.")
        
    else:
        return render(request, 'auth_user_app/login.html',{}) # pass empty dict if you want