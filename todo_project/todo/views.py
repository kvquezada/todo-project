from django.shortcuts import render

from .models import Todo


def todo_list_view(request):
  context ={}
  context['dataset'] = Todo.objects.all()

  return render(request, 'pages/todo.html', context)
