# Generated by Django 4.1.4 on 2022-12-26 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_hotels_details_image_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotels_details',
            name='Image_url',
        ),
    ]
