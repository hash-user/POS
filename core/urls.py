from django.urls import path
from . import views

urlpatterns = [
	path('login', views.login, name='login.html'),
	path('dashboard', views.dashboard, name='dashboard.html'),
	path('registration', views.registration, name='registration.html'),
	path('searchinfo', views.searchinfo, name='search-info.html'),
	path('add-new-pos', views.newpos, name='add-new-pos.html'),
	path('add-new-user', views.newuser, name='add-new-user.html'),
]

