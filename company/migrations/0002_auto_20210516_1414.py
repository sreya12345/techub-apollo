# Generated by Django 3.2.3 on 2021-05-16 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spglobal',
            name='environmental_score',
            field=models.CharField(max_length=4096),
        ),
        migrations.AlterField(
            model_name='spglobal',
            name='governance_score',
            field=models.CharField(max_length=4096),
        ),
        migrations.AlterField(
            model_name='spglobal',
            name='social_score',
            field=models.CharField(max_length=4096),
        ),
    ]