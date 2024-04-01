# Generated by Django 5.0.3 on 2024-04-01 11:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_remove_userpayment_user_remove_userprofile_user_and_more'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('status', models.BooleanField(default=False)),
                ('products', models.ManyToManyField(related_name='orders', to='products.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
