# Generated by Django 4.0.1 on 2022-03-17 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0020_rename_date_of_birth_staffdetails_date_of_joining'),
    ]

    operations = [
        migrations.CreateModel(
            name='patent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('members', models.CharField(default='', max_length=200)),
                ('date', models.DateField(default='2000-12-31')),
            ],
        ),
    ]
