# Generated by Django 4.0.1 on 2022-03-30 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0043_alter_messagebox_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='admissionform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(default='', max_length=500)),
                ('Branch', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
