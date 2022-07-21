from django.urls import path,include
from usermanagement import views
from django.contrib import admin


urlpatterns = [
    # path('',views.home, name='home'),
    path('register/',views.register, name="register"),
    path('',views.user_login, name='user_login'),
    path('logout/',views.user_logout, name='user_logout'),
    path("password_reset/", views.password_reset_request, name="password_reset"),
    
]
