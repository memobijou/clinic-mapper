# Generated by Django 2.1.7 on 2019-07-06 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account_mapping', '0005_mandator_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mandator',
            name='account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mandators', to='account_mapping.AccountMapping'),
        ),
    ]
