from django.urls import path
from . import views

urlpatterns = [
    path('todosite/', views.submit, name="todosite"),
    path('del/<int:item_id>', views.remove, name="delete"),
    path('setuptask/', views.SetUpTask.as_view(), name="setuptask"),
]
