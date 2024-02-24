from django.urls import path
from webapp.views import index_view, create_task_view, task_view, update_task_view, task_delete_view

urlpatterns = [
    path('', index_view, name='index'),
    path('task/add/', create_task_view, name='task_create'),
    path('task/<int:pk>', task_view, name='task_view'),
    path('task/<int:pk>/update', update_task_view, name='task_update'),
    path('task/<int:pk>/delete/', task_delete_view, name='task_delete')
]