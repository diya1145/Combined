# Generated by Django 4.2.4 on 2023-08-24 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_delete_post1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]