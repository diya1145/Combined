# Generated by Django 4.2.4 on 2023-08-24 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
