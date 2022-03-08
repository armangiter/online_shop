# Generated by Django 4.0.2 on 2022-03-03 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('delete_timestamp', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, help_text='This is deleted datetime', null=True, verbose_name='Deleted Datetime')),
                ('is_deleted', models.BooleanField(default=False, help_text='This is deleted status', verbose_name='Deleted status')),
                ('is_active', models.BooleanField(default=True, help_text='This is active status', verbose_name='Active status')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='slug')),
                ('root', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('delete_timestamp', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, help_text='This is deleted datetime', null=True, verbose_name='Deleted Datetime')),
                ('is_deleted', models.BooleanField(default=False, help_text='This is deleted status', verbose_name='Deleted status')),
                ('is_active', models.BooleanField(default=True, help_text='This is active status', verbose_name='Active status')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='slug')),
                ('image', models.ImageField(upload_to='products/%Y/%m/%d', verbose_name='image')),
                ('descriptions', models.TextField(verbose_name='descriptions')),
                ('price', models.IntegerField(verbose_name='price')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.category', verbose_name='category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ('name',),
            },
        ),
    ]
