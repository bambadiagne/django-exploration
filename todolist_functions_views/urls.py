from django.urls import include, path
from . import views

urlpatterns = [

    path('',views.list,name="list_tasks"),
    path('add',views.add,name='add_task')
    path('update/<int:id>',views.update,name='update_task')
    path("delete/<int:id>",views.delete,name='delete_task')
]
