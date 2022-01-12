from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.title} {self.contents}"
        
