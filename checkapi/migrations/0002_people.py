# Generated by Django 5.0.6 on 2024-07-06 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
