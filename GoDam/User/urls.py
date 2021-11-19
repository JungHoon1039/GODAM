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
        path('info',views.userinfo),
        path('edit',views.password_edit),
        path('edit_com',views.password_edit_complete),
        path('delete',views.member_delete),
        path('delete_com',views.member_delete_complete),

]
