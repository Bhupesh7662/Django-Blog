from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Index, name="Index"),
    path('news/<slug:slug>', views.news, name="news"),
    path('subcategory/', views.subcategory, name='subcategory'),
    path('manage_post/', views.manage_post, name='manage_post'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit_post/<int:id>', views.edit_post, name='edit_post'),
    path('delete_post/<int:id>', views.delete_post, name='delete_post'),
    path('display_comments/', views.display_comments, name='display_comments'),
    path('delete_comment/<int:id>', views.delete_comment, name='delete_comment'),
]
