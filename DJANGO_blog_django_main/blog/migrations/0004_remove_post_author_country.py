# Generated by Django 4.2.2 on 2024-01-04 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author_country',
        ),
    ]
