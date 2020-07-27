from django.db import models
from datetime import datetime
class Task(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField()
    date=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
