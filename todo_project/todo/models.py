from django.db import models
from django.contrib.auth.models import User
from todo_project.users.models import User

class Todo(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
  title = models.CharField(max_length=100)
  due_date = models.DateField()

  def __str__(self):
      return self.title
