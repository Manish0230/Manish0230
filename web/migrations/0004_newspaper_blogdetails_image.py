# Generated by Django 4.0.1 on 2022-03-01 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_blogdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='newspaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(default='', max_length=30)),
                ('ocassion', models.CharField(default='', max_length=30)),
                ('date', models.DateField(default='2000-12-31')),
                ('name', models.CharField(default='', max_length=30)),
                ('image', models.ImageField(default='', upload_to='newspaper/images')),
            ],
        ),
        migrations.AddField(
            model_name='blogdetails',
            name='image',
            field=models.ImageField(default='', upload_to='newspaper/images'),
        ),
    ]
