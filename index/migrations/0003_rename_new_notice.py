# Generated by Django 4.0.6 on 2022-08-07 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_new_delete_news'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='New',
            new_name='Notice',
        ),
    ]