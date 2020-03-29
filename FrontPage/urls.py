from django.conf.urls import url
from . import views
urlpatterns = [
    url('Login', views.Login, name='Login'),
    url('Sign', views.Signup, name='Signup'),
    url('Logout', views.Logout, name='Home')
]
