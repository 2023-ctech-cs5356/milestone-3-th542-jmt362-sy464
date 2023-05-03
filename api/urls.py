from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addItem),
    path('delete/<int:post_id>', views.deleteItem, name='delete-item'),
]