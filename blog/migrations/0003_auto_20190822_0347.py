# Generated by Django 2.2.1 on 2019-08-22 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190822_0258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='pub_data',
            new_name='pub_date',
        ),
    ]
