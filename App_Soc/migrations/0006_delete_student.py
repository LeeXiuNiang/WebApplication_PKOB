# Generated by Django 3.2.8 on 2021-11-19 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Soc', '0005_rename_users_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]