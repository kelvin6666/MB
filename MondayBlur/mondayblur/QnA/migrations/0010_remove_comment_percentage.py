# Generated by Django 2.2 on 2019-05-18 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QnA', '0009_auto_20190518_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='percentage',
        ),
    ]
