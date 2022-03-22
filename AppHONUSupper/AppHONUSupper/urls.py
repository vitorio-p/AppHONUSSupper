"""AppStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
	re_path(r'^$', views.index, name='home'),
	re_path(r'ride', views.ride, name='ride'),
	re_path(r'driver', views.driver, name='driver'),
	re_path(r'loginhome', views.loginhome, name='loginhome'),
	re_path(r'login', auth_views.LoginView.as_view(template_name='AppHONUSupper/login.html'), name='login'),
	re_path(r'logout', auth_views.LogoutView.as_view(template_name='AppHONUSupper/logout.html'), name='logout'),
	re_path(r'register', views.register, name='register'),
	re_path(r'profile', views.profile, name='profile'),
	re_path(r'advertise', views.advertise, name='advertise'),
	re_path(r'bid', views.bid, name='bid'),
	re_path(r'acceptance', views.acceptance, name='acceptance'),
	"""
    path('admin/', admin.site.urls), #old
    path('', app.views.index, name='index'),
    path('add', app.views.add, name='add'),
    path('view/<str:id>', app.views.view, name='view'),
    path('edit/<str:id>', app.views.edit, name='edit'),
    """
]
