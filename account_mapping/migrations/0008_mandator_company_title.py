# Generated by Django 2.1.7 on 2019-08-23 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_mapping', '0007_auto_20190823_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='mandator',
            name='company_title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]