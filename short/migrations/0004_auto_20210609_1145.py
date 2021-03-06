# Generated by Django 3.0.11 on 2021-06-09 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0003_user_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign',
            name='username',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.ForeignKey(default='unknown', on_delete=django.db.models.deletion.CASCADE, to='short.Sign'),
        ),
    ]
