# Generated by Django 3.2.8 on 2021-10-16 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_foods', '0004_auto_20211016_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
