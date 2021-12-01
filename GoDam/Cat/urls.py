from django.urls import path
from . import views

urlpatterns = [
        path('newcat', views.catupload),
        path('catadded', views.catuploaded),
        path('allcat',views.catall),
        path('cat/<int:Catid>',views.cat,name="cat"),
        path('cat/<int:Catid>/edit',views.catedit,name="catedit"),
        path('cateditok',views.cateditok),
        path('cat/<int:Catid>/delete',views.catdelete,name="catdelete")
]
