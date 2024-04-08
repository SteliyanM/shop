# Generated by Django 5.0.3 on 2024-04-08 15:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(error_messages={'max_length': 'bokatas_store.categories.models name must conatain max 50', 'unique': 'bokatas_store.categories.models with that name already exists'}, max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(limit_value=3, message='bokatas_store.categories.models name must contain at latest 3')])),
                ('picture', models.ImageField(upload_to='category_pictures')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
