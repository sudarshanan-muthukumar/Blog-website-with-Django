# Generated by Django 4.1.3 on 2022-11-30 08:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_blog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 11, 30, 8, 10, 10, 980098)),
        ),
    ]
