# Generated by Django 4.0.3 on 2022-05-02 07:28

from django.db import migrations
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userinfo'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', users.models.UserManager()),
            ],
        ),
    ]