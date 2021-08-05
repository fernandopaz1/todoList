from django.urls import path
from . import views

APP_NAME = 'todo'
urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('todo/<int:pk>/', views.todo_details, name='todo_detail'),
    path('delete/<int:pk>/', views.todo_delete, name='todo_delete'),
    path('change/<int:pk>/<str:state>', views.change_state, name='change_state'),
]

