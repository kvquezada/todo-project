from django.urls import path

from .views import todo_list_view

app_name = 'todo'

urlpatterns = [
  path("", todo_list_view, name="todo"),
]