# Generated by Django 4.0.6 on 2022-07-18 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_patron',
            new_name='is_creator',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_user',
            new_name='is_member',
        ),
    ]