# Generated by Django 4.0.5 on 2022-06-08 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta_app', '0015_remove_comment_user_id_remove_picture_likes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='commentor',
        ),
    ]