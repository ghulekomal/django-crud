# Generated by Django 3.0.7 on 2020-06-26 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fullname', models.CharField(max_length=100)),
                ('Emp_code', models.CharField(max_length=3)),
                ('Mobile', models.CharField(max_length=15)),
                ('Position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_register.Position')),
            ],
        ),
    ]