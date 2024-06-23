# Generated by Django 5.0.6 on 2024-06-22 17:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_medicine_medicine_desc_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_first_name', models.CharField(max_length=20)),
                ('customer_last_name', models.CharField(max_length=20)),
                ('customer_address', models.CharField(max_length=20)),
                ('customer_contact', models.IntegerField()),
                ('customer_email', models.EmailField(max_length=254)),
            ],
            options={
                'ordering': ['customer_first_name'],
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('purchase_contact', models.IntegerField()),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchase_quantity', models.PositiveIntegerField()),
                ('purchase_customer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.customer')),
            ],
            options={
                'ordering': ['product_name'],
            },
        ),
    ]