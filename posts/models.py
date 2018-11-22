from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):

    PUBLISHED = 'PUB'
    DRAFT = 'DRA'
    STATUS = (
        (PUBLISHED, 'Published'),
        (DRAFT, 'Draft')
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    intro = models.CharField(max_length=300)
    body = models.TextField()
    image = models.FileField()
    status = models.CharField(max_length=3, choices=STATUS, default=DRAFT)
    publication_date = models.DateTimeField(null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0} ({1})'.format(self.title, self.get_status_display())
