# Generated by Django 4.0.5 on 2022-06-05 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='picture',
            old_name='name',
            new_name='title',
        ),
    ]
