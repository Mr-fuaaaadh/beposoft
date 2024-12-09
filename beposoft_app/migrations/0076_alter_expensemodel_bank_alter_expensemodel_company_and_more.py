# Generated by Django 5.1.3 on 2024-12-09 06:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beposoft_app', '0075_alter_expensemodel_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensemodel',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='banks', to='beposoft_app.bank'),
        ),
        migrations.AlterField(
            model_name='expensemodel',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='beposoft_app.company'),
        ),
        migrations.AlterField(
            model_name='expensemodel',
            name='payed_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payed_by', to='beposoft_app.user'),
        ),
    ]
