# Generated by Django 3.2 on 2021-05-09 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobile',
            name='specs',
            field=models.CharField(default='', max_length=30),
        ),
    ]