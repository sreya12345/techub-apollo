# Generated by Django 3.2.3 on 2021-05-16 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20210516_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spglobal',
            name='industry',
            field=models.CharField(max_length=4096),
        ),
    ]