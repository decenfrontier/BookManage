# Generated by Django 3.2.5 on 2021-07-06 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('view', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='name',
            field=models.CharField(max_length=20, unique=True, verbose_name='名称'),
        ),
    ]