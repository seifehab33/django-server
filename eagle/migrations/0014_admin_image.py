# Generated by Django 5.0.4 on 2024-05-07 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eagle', '0013_merge_20240501_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='admin_images/'),
        ),
    ]
