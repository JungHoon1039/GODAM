from django.urls import path
from . import views

urlpatterns = [
        path('signup', views.signup, name='signup'),
        path('signup_com', views.signup_com, name='signup_com'),
        path('check_id',views.check_id, name='check_id'),
        path('login',views.login, name='login'),
        path('logged', views.logged, name='logged'),
        path('logout', views.logout, name='logout'),
        path('info',views.userinfo, name='info'),
        path('delete_com',views.member_delete_complete, name='delete_com'),
        path('edit',views.info_edit, name='edit'),
        path('edit_com',views.info_edit_complete, name='edit_com'),
        path('password_edit',views.password_edit, name='password_edit'),
        path('password_edit_com',views.password_edit_complete, name='password_edit_com'),
        path('about', views.about, name='about'),
        path('aboutus', views.aboutus, name='aboutus'),
        path('index', views.index, name='index'),
        path('aboutlan',views.aboutlan, name="aboutlan")
]
