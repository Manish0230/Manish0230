# Generated by Django 4.0.1 on 2022-03-17 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0022_patent_patentnumber_patent_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='alumini',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default='2000-12-31')),
                ('name', models.CharField(default='', max_length=30)),
                ('details', models.CharField(default='', max_length=200)),
                ('image', models.ImageField(default='', upload_to='alumini/images')),
            ],
        ),
    ]
