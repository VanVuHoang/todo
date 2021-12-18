from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    # author = models.CharField(max_length = 50)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}  {self.contents}"


class CheckIn(models.Model):
    check = models.BooleanField()

    def __str__(self):
        return f"{self.check}"
