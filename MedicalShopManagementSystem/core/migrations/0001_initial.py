# Generated by Django 5.0.6 on 2024-06-18 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealer_name', models.CharField(max_length=20)),
                ('dealer_address', models.TextField(max_length=70)),
                ('dealer_number', models.IntegerField(max_length=12)),
                ('dealer_email', models.EmailField(max_length=20)),
            ],
        ),
    ]
