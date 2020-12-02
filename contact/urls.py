from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('feedback/', views.feedback, name='feedback'),
    path('delete_feedback/<int:id>', views.delete_feedback, name='delete_feedback'),
]
