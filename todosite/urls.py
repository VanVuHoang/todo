from django.urls import path
from . import views

urlpatterns = [
    path('todosite/', views.submit, name="todosite"),
    path('del/', views.removetask, name="delete"),
    path('upd/11', views.updatetask, name="update"),
    path('add/', views.addtask, name="add"),
]
