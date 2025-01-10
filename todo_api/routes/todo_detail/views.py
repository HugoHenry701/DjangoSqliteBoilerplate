from django.core.serializers import serialize
from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from todo_api.models import Todo
from todo_api.serializers import TodoSerializer


class TodoDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # 1. get object function
    def get_object(self, todo_id, user_id):
        """
        Helper method to get the object with given todo_id, and user_id
        """
        try:
            return Todo.objects.get(id=todo_id, user=user_id)
        except Todo.DoesNotExist:
            return None

    # 2. Get API
    def get(self, request, todo_id, *args, **kwargs):
        """
        Retrieves the Todo with given todo_id
        """
        todo_instance = self.get_object(todo_id, request.user.id)
        if not todo_instance:
            return Response({"res": "Object with todo id does not exists"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(todo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
