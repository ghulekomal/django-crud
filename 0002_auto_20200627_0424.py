# Generated by Django 3.0.7 on 2020-06-27 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Fullname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Position',
            field=models.CharField(max_length=15),
        ),
        migrations.DeleteModel(
            name='Position',
        ),
    ]
