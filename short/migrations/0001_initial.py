# Generated by Django 3.0.11 on 2021-06-03 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.URLField()),
                ('s_name', models.CharField(max_length=40)),
            ],
        ),
    ]
