# Generated by Django 4.2.7 on 2023-11-29 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SuperHeroes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hero',
            old_name='strength3',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='hero',
            old_name='weakness2',
            new_name='food',
        ),
        migrations.RenameField(
            model_name='hero',
            old_name='imagePath',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='hero',
            old_name='weakness1',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='hero',
            old_name='weakness3',
            new_name='music',
        ),
        migrations.RenameField(
            model_name='hero',
            old_name='realName',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='hero',
            old_name='strength1',
            new_name='strength',
        ),
        migrations.RenameField(
            model_name='hero',
            old_name='strength2',
            new_name='weakness',
        ),
    ]