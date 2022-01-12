from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit, name="todosite"),
    path('del/<int:item_id>', views.remove, name="delete"),
]
