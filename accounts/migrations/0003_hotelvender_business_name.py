# Generated by Django 5.2.4 on 2025-07-24 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_hoteluser_is_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelvender',
            name='business_name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
