# Generated by Django 2.1.3 on 2018-11-24 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20181124_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(blank=True, max_length=3),
        ),
    ]