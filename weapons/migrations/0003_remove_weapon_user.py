# Generated by Django 4.2.5 on 2023-09-26 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weapons', '0002_weapon_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weapon',
            name='user',
        ),
    ]
