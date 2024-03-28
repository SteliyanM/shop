# Generated by Django 5.0.3 on 2024-03-27 16:15

import django.core.validators
import django.db.models.deletion
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
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(error_messages={'max_length': 'bokatas_store.products.models name must conatain max 50', 'unique': 'bokatas_store.products.models with that name already exists'}, max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(limit_value=3, message='bokatas_store.products.models name must contain at latest 3')])),
                ('picture', models.ImageField(upload_to='mediafiles/category_pictures')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductPictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='mediafiles/product_pictures')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(error_messages={'max_length': 'bokatas_store.products.models name must conatain max 50'}, max_length=50, validators=[django.core.validators.MinLengthValidator(limit_value=3, message='bokatas_store.products.models name must contain at latest 3')])),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('count', models.SmallIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('pictures', models.ManyToManyField(related_name='products', to='products.productpictures')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
