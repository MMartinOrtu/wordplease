from django.db import models

class Post(models.Model):

    PUBLISHED = 'PUB'
    DRAFT = 'DRA'
    STATUS = (
        (PUBLISHED, 'Published'),
        (DRAFT, 'Draft')
    )

    title = models.CharField(max_length=150)
    intro = models.CharField(max_length=300)
    body = models.TextField()
    image = models.FileField()
    status = models.CharField(max_length=3, choices=STATUS, default=DRAFT)

    def __str__(self):
        return '{0} ({1})'.format(self.title, self.get_status_display())
