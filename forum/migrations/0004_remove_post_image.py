# Generated by Django 4.0.6 on 2022-08-25 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_post_image_alter_post_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
