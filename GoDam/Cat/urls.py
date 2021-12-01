from django.urls import path
from . import views

urlpatterns = [
        path('newcat', views.catupload),
        path('allcat',views.catall),
        path('cat/<int:Catid>',views.cat,name="cat"),
        path('cat/<int:Catid>/edit',views.catedit,name="catedit"),
        path('cat/<int:Catid>/delete',views.catdelete,name="catdelete"),
        path('options', views.options),
        path('write', views.writePage, name='create_contentView'),
        path('list', views.listPage, name='list_contentView'),
        path('view/<int:id>', views.showContent, name='show_contentView'),
        path('modify/<int:id>', views.modifyContent, name='modify_contentView'),
        path('delete/<int:id>', views.deleteContent, name='delete_contentView'),
]
