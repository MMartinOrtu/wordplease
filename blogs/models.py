from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    publication_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Blog {0} de ({1})'.format(self.owner, self.title)
