from django.urls import path
from todo_api.routes.todo_list.views import (
    TodoListApiView
)
from todo_api.routes.todo_detail.views import (
    TodoDetailApiView
)

urlpatterns = [
    path('api', TodoListApiView.as_view()),
    path('api/<int:todo_id>/', TodoDetailApiView.as_view())
]
