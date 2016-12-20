from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=200)
    comment = models.TextField()
    pub_date = models.DateField()
