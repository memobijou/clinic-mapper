# Generated by Django 2.1.7 on 2019-07-06 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_mapping', '0002_mandator'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountmapping',
            name='mandators',
            field=models.ManyToManyField(to='account_mapping.Mandator'),
        ),
    ]
