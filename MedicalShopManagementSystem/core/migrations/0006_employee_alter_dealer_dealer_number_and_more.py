# Generated by Django 5.0.6 on 2024-06-22 11:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_medicine_medicine_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField(unique=True)),
                ('employee_first_name', models.CharField(max_length=20)),
                ('employee_last_name', models.CharField(max_length=20)),
                ('employee_address', models.CharField(max_length=20)),
                ('employee_salary', models.IntegerField()),
                ('employee_contact', models.IntegerField()),
                ('employee_email', models.EmailField(max_length=254)),
            ],
            options={
                'ordering': ['employee_id'],
            },
        ),
        migrations.AlterField(
            model_name='dealer',
            name='dealer_number',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='medicine_dealer_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicines', to='core.dealer'),
        ),
    ]