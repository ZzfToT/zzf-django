# Generated by Django 3.2.8 on 2023-06-19 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_post_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='mdfile',
        ),
    ]