# Generated by Django 3.2.4 on 2021-10-06 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineOrder', '0004_invoice_sub_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='sub_total',
            field=models.CharField(max_length=1000),
        ),
    ]
