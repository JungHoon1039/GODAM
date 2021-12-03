from django.urls import path
from . import views

urlpatterns = [
        path('allcat',views.catall),
        path('cat/<int:Catid>',views.cat,name="cat"),
        path('cat/<int:Catid>/edit',views.catedit,name="catedit"),
        path('cat/<int:Catid>/delete',views.catdelete,name="catdelete"),
        path('cat/<int:Catid>/<int:Boardid>', views.bd, name="bd"),
]