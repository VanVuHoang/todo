from django.urls import path
from . import views

urlpatterns = [
    path('', views.site, name="site"),
    path('todosite/', views.submit, name="todosite"),
    path('del/<int:item_id>', views.deletetask, name="delete"),
    path('del/', views.deleteall, name="deleteall"),
    path('todosite/upd/<int:item_id>', views.updatetask, name="updatetask"),
    path('upd/<int:item_id>', views.updatetask, name="update"),
]