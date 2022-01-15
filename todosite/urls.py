from django.urls import path
from . import views

urlpatterns = [
    path('todosite/', views.submit, name="todosite"),
    path('del/<int:item_id>', views.removetask, name="delete"),
    path('delall/', views.deleteall, name="deleteall"),
]
