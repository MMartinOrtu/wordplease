# Generated by Django 2.1.3 on 2018-11-25 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0016_post_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='blog',
        ),
    ]
