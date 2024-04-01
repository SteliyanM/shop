# Generated by Django 5.0.3 on 2024-04-01 11:23

import django.core.validators
import django.db.models.deletion
import django_countries.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_remove_userpayment_user_remove_userprofile_user_and_more'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('address1', models.CharField(max_length=1024, verbose_name='Address line 1')),
                ('address2', models.CharField(max_length=1024, verbose_name='Address line 2')),
                ('zip_code', models.CharField(max_length=12, verbose_name='ZIP / Postal code')),
                ('city', models.CharField(max_length=1024, verbose_name='City')),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator(message='First name can contain only letters', regex='^[a-zA-Z]+$')])),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator(message='Last name can contain only letters', regex='^[a-zA-Z]+$')])),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other'), ('prefer not to say', 'Prefer Not To Say')], max_length=20, null=True)),
                ('profile_picture', models.ImageField(default='profile_pictures/default_profile_picture.webp', upload_to='profile_pictures')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserPayment',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('payment_method', models.CharField(choices=[('credit card', 'Credit Card'), ('paypal', 'Paypal'), ('bank transfer', 'Bank Transfer'), ('cash', 'Cash')], default='credit card', max_length=20)),
                ('is_successful', models.BooleanField(default=False)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
