# Generated by Django 4.2.4 on 2023-10-01 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('heropk', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('realName', models.CharField(max_length=200)),
                ('strength1', models.CharField(max_length=200)),
                ('strength2', models.CharField(max_length=200)),
                ('strength3', models.CharField(max_length=200)),
                ('weakness1', models.CharField(max_length=200)),
                ('weakness2', models.CharField(max_length=200)),
                ('weakness3', models.CharField(max_length=200)),
                ('imagePath', models.CharField(max_length=200)),
            ],
        ),
    ]
