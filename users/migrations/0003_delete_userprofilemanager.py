# Generated by Django 3.0.6 on 2020-08-03 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200803_2158'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfileManager',
        ),
    ]
