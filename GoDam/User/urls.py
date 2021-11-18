from django.urls import path
from . import views

urlpatterns = [
        path('catsignup', views.cat_signup),
        path('catsignup_com', views.cat_signup_com),
        path('catlogin',views.cat_login),
        path('catindex', views.cat_index),
        path('catlogged', views.cat_logged),
        path('catlogout', views.cat_logout),
]
