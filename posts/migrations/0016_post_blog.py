# Generated by Django 2.1.3 on 2018-11-25 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
        ('posts', '0015_auto_20181124_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='blog',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blogs.Blog'),
            preserve_default=False,
        ),
    ]
