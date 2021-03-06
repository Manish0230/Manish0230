# Generated by Django 4.0.1 on 2022-03-07 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_company_alter_blogdetails_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='placement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('package', models.CharField(default='', max_length=30)),
                ('company_name', models.CharField(default='', max_length=30)),
                ('candidate_details', models.CharField(default='', max_length=200)),
                ('Date_of_allotment', models.DateField(default='2000-12-31')),
                ('jobpost', models.CharField(default='', max_length=100)),
                ('Eductaion', models.CharField(default='', max_length=300)),
                ('Subject', models.CharField(default='', max_length=100)),
                ('review_by_interviewer', models.CharField(default='', max_length=300)),
                ('image', models.ImageField(default='', upload_to='placement/images')),
            ],
        ),
        migrations.CreateModel(
            name='placementdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companies_visited', models.CharField(default='', max_length=30)),
                ('averagepackage', models.CharField(default='', max_length=200)),
                ('highestpackage', models.CharField(default='', max_length=30)),
                ('numberofplacement', models.CharField(default='', max_length=30)),
            ],
        ),
    ]
