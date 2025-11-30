from django import forms
from django.contrib.auth.models import User
from auth_user_app.models import UserProfileInfo


# model means standard data table
# ModelForm means form for user input

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ('username', 'email', 'password')
        
        
class UserProfileInfoForm(forms.ModelForm):
    
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')