# Generated by Django 3.1.5 on 2021-01-22 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=99)),
                ('length', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ArticleWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(blank=True, null=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='words.article')),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='words.word')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='words',
            field=models.ManyToManyField(through='words.ArticleWord', to='words.Word'),
        ),
    ]
