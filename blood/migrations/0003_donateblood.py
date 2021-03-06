# Generated by Django 3.0.5 on 2020-08-22 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0002_auto_20200822_2308'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonateBlood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=50)),
                ('person_email', models.CharField(default='', max_length=50)),
                ('person_mobileNumber', models.IntegerField(default=0)),
                ('person_age', models.IntegerField(default=0)),
                ('person_address', models.CharField(max_length=200)),
                ('person_gender', models.CharField(max_length=20)),
                ('person_bloodGroup', models.CharField(max_length=20)),
            ],
        ),
    ]
