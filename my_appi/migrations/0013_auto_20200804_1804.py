# Generated by Django 3.0.6 on 2020-08-04 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_appi', '0012_auto_20200803_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_appi.Topic'),
        ),
    ]