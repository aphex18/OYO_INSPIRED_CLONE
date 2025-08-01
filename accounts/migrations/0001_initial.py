# Generated by Django 5.2.4 on 2025-07-23 10:55

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.ImageField(upload_to='images/hotels/amenities_icons/')),
            ],
        ),
        migrations.CreateModel(
            name='HotelUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profile_picture', models.ImageField(upload_to='images/profile_pics/user/')),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('email_token', models.CharField(blank=True, max_length=100, null=True)),
                ('otp', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='HotelVender',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profile_picture', models.ImageField(upload_to='images/profile_pics/vendor/')),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('email_token', models.CharField(blank=True, max_length=100, null=True)),
                ('otp', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=200)),
                ('hotel_description', models.TextField()),
                ('hotel_slug', models.SlugField(max_length=191, unique=True)),
                ('hotel_price', models.FloatField()),
                ('hotel_offer_price', models.FloatField()),
                ('hotel_location', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('amenities', models.ManyToManyField(to='accounts.amenities')),
                ('hotel_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotels', to='accounts.hotelvender')),
            ],
        ),
        migrations.CreateModel(
            name='HotelImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/hotels/hotel_images/')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotels_images', to='accounts.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='HotelManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager_name', models.CharField(max_length=100)),
                ('manager_contact', models.CharField(max_length=100)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_managers', to='accounts.hotel')),
            ],
        ),
    ]
