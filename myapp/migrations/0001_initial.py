# Generated by Django 4.2 on 2024-11-22 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usersignup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('mobile', models.BigIntegerField()),
                ('username', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=12)),
            ],
        ),
    ]
