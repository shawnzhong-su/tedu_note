# Generated by Django 4.2.9 on 2024-02-14 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=32, verbose_name='passWord')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='createTime')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='updatedTime')),
            ],
        ),
    ]
