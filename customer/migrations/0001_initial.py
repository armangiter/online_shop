# Generated by Django 4.0.2 on 2022-02-28 10:32

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
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('phone', models.CharField(max_length=13, unique=True, verbose_name='Phone')),
                ('full_name', models.CharField(max_length=255, verbose_name='Full Name')),
                ('is_active', models.BooleanField(default=True, help_text='is user an active user', verbose_name='Is Active')),
                ('is_admin', models.BooleanField(default=False, help_text='is user an admin', verbose_name='Is Admin')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
