# Generated by Django 4.2.1 on 2023-05-12 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('college_name', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Colleges',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course_name', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('email_address', models.CharField(max_length=300)),
                ('year_level', models.CharField(max_length=20)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simple_profiling.college')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simple_profiling.course')),
            ],
            options={
                'verbose_name_plural': 'Students',
            },
        ),
    ]