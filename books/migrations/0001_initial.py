# Generated by Django 5.1.7 on 2025-04-01 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('rating', models.FloatField()),
                ('genre', models.CharField(max_length=30)),
                ('release_year', models.DateField()),
                ('author', models.CharField(max_length=50)),
                ('pages', models.SmallIntegerField()),
                ('language', models.CharField(max_length=15)),
                ('isbn', models.CharField(max_length=50)),
            ],
        ),
    ]
