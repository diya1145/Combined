# Generated by Django 3.2.12 on 2023-08-25 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.tags'),
            preserve_default=False,
        ),
    ]