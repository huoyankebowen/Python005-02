# Generated by Django 2.2.13 on 2020-12-21 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('douban', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='updated_date',
            field=models.CharField(max_length=20),
        ),
    ]
