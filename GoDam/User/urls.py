from django.urls import path
from . import views

urlpatterns = [
        path('signup', views.signup),
        path('signup_com', views.signup_com),
        path('login',views.login),
        path('index', views.index),
        path('logged', views.logged),
        path('logout', views.logout),
        path('check_id',views.check_id),
]
