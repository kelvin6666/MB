# Generated by Django 2.1.7 on 2019-05-22 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QnA', '0012_comment_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='image',
        ),
    ]
