from django.urls import path
from . import views

urlpatterns = [
    path('todosite/', views.submit, name="todosite"),
    path('del/<int:item_id>', views.removetask, name="delete"),
    path('del/', views.deleteall, name="deleteall"),
    path('todosite/upd/<int:item_id>', views.updatetask, name="update"),
    path('upd/<int:item_id>', views.updatetask, name="update"),
]
