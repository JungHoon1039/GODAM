from django.urls import path
from . import views

urlpatterns = [
        path('newcat', views.catupload),
        path('catadded', views.catuploaded)
]
