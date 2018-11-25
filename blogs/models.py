from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Blog(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    publication_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created or not hasattr(instance, 'blog'):
            Blog.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.blog.title = '{0}'.format(instance.blog)
        instance.blog.save()

    def __str__(self):
        return 'The blog of {0}'.format(self.user)
