# from django.db import models
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# model means standard data table
# ModelForm means form for user input

class UserProfileInfo(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)  # create relation with User (from django.contrib.auth.models import User)
    # OneToOneField is used to create a one to one relationship between two models 
    # since User table in sql table by default django create it, so we dont need to create it again and we just use one to one field
    
    # additional classes
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True) # 'profile_pics' must match with the under media folder name
    
    def __str__(self):
        return self.user.username