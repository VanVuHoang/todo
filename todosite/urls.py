from django.urls import path
from . import views
urlpatterns = [
    path('todosite/', views.submit, name="todosite"),
]