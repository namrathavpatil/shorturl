# Generated by Django 3.0.11 on 2021-06-09 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0004_auto_20210609_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.ForeignKey(default='unknown', on_delete=django.db.models.deletion.CASCADE, to='short.Sign'),
        ),
    ]
