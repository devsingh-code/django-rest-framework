# Generated by Django 3.0.7 on 2020-06-14 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='owner',
        ),
    ]