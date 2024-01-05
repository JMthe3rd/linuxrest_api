from datetime import date
from django.contrib.auth.models import User
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    created_at = models.DateField(default=date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)

    def time_passed(self):
        today = date.today()
        delta = today - self.created_at
        return delta.days