# Generated by Django 3.2.2 on 2021-05-07 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerenquiry',
            name='queries',
            field=models.CharField(max_length=500),
        ),
    ]