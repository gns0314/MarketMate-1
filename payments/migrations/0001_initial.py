# Generated by Django 4.2.4 on 2023-08-24 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imp_uid', models.CharField(max_length=100)),
                ('merchant_uid', models.CharField(max_length=100)),
                ('amount', models.PositiveIntegerField()),
                ('status', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
