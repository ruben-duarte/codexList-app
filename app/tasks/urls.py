from django.urls import path
from . views import List_tasks, Create_tasks, Delete_tasks


urlpatterns = [
    path('', List_tasks ),
    path("new/", Create_tasks, name="create_tasks"),
    path('delete_task/<int:task_id>/', Delete_tasks, name="delete_task")

]
