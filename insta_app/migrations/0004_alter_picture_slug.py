# Generated by Django 4.0.5 on 2022-06-06 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta_app', '0003_like_follow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='slug',
            field=models.SlugField(max_length=100, null=True),
        ),
    ]
