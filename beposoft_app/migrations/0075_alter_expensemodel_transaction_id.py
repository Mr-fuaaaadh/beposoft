# Generated by Django 5.1.3 on 2024-12-09 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beposoft_app', '0074_alter_warehousedata_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensemodel',
            name='transaction_id',
            field=models.CharField(max_length=100),
        ),
    ]
