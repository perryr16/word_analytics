# Generated by Django 3.1.5 on 2021-01-26 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0010_articleword_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleword',
            name='content',
            field=models.TextField(default=None),
        ),
    ]
