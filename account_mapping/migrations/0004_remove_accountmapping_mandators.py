# Generated by Django 2.1.7 on 2019-07-06 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account_mapping', '0003_accountmapping_mandators'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountmapping',
            name='mandators',
        ),
    ]
