# Generated by Django 2.1.7 on 2019-08-23 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_mapping', '0008_mandator_company_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mandator',
            name='account',
        ),
        migrations.AddField(
            model_name='mandator',
            name='account',
            field=models.ManyToManyField(null=True, related_name='mandators', to='account_mapping.AccountMapping'),
        ),
    ]
