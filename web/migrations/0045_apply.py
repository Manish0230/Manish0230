# Generated by Django 4.0.1 on 2022-03-31 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0044_admissionform'),
    ]

    operations = [
        migrations.CreateModel(
            name='apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(default='', max_length=100)),
                ('Lastname', models.CharField(default='', max_length=100)),
                ('City', models.CharField(default='', max_length=100)),
                ('Contactnumber', models.CharField(default='', max_length=100)),
                ('course', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
