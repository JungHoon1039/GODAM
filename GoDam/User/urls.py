from django.urls import path
from . import views

urlpatterns = [
        path('signup', views.signup),
        path('signup_com', views.signup_com),
        path('check_id',views.check_id),
        path('login',views.login),
        path('logged', views.logged),
        path('logout', views.logout),
        path('info',views.userinfo),
        path('delete_com',views.member_delete_complete),
        path('edit',views.info_edit),
        path('edit_com',views.info_edit_complete),
        path('password_edit',views.password_edit),
        path('password_edit_com',views.password_edit_complete),
        path('about', views.about),
        path('aboutus', views.aboutus),
        path('index', views.index),
        path('map', views.mapp),
]
