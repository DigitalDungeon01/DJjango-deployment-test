from django.urls import path
from auth_user_app import views

# template urls
app_name = 'auth_user_app'

urlpatterns = [
    path('register/', views.register, name='register'),
    # path('user_login/', views.user_login, name='user_login'),
    path('user_login/', views.user_login, name='user_login'),
    
]