# Generated by Django 4.2.1 on 2023-05-12 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_profiling', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='year_level',
            field=models.CharField(choices=[('1st Year', '1st Year'), ('2nd Year', '2nd Year'), ('3rd Year', '3rd Year'), ('4th Year', '4th Year')], max_length=20),
        ),
    ]