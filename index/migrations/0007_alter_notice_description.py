# Generated by Django 4.0.6 on 2022-09-05 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_notice_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
