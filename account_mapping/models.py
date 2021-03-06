from django.db import models


class AccountMapping(models.Model):
    email = models.EmailField(blank=False, null=True)
    url = models.CharField(blank=False, null=True, max_length=200)


class Mandator(models.Model):
    company_title = models.CharField(blank=False, null=True, max_length=200)
    url = models.CharField(blank=False, null=True, max_length=200)
    account = models.ManyToManyField("account_mapping.AccountMapping", null=True, blank=False, related_name="mandators")
    theme = models.CharField(blank=False, null=True, max_length=200)
    logo_url = models.CharField(blank=False, null=True, max_length=200)
