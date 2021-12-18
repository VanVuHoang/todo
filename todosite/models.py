from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100, default='DEFAULT VALUE')
    contents = models.TextField(default='DEFAULT VALUE')
    date = models.DateTimeField(auto_now=True, null=True)
    check = models.BooleanField()

    def __str__(self):
        return f"{self.title} {self.contents} {self.check}"
