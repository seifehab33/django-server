# Generated by Django 5.0.4 on 2024-05-12 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eagle', '0016_rename_phone_number_contactmessage_phoneno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='phoneno',
            field=models.IntegerField(max_length=20),
        ),
    ]
