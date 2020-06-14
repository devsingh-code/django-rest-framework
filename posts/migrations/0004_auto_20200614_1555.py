# Generated by Django 3.0.7 on 2020-06-14 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200613_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('D', 'Django'), ('R', 'React')], max_length=3),
        ),
        migrations.AlterField(
            model_name='post',
            name='custom_id',
            field=models.IntegerField(),
        ),
    ]
