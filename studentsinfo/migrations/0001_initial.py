# Generated by Django 4.0.5 on 2022-07-01 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('student_id', models.IntegerField(default=0)),
                ('phone', models.CharField(max_length=15)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentsinfo.department')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentsinfo.section')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentsinfo.semester')),
            ],
        ),
    ]
