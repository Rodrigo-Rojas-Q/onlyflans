# Generated by Django 3.2 on 2024-08-07 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='public_bio',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='public_birth_date',
            field=models.BooleanField(default=True),
        ),
    ]
