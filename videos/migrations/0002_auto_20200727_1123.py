# Generated by Django 3.0.3 on 2020-07-27 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movies',
            old_name='lenght',
            new_name='length',
        ),
    ]
