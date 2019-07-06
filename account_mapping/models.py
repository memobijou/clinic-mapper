from django.db import models


class AccountMapping(models.Model):
    email = models.EmailField(blank=False, null=True)
    url = models.CharField(blank=False, null=True, max_length=200)


class Mandator(models.Model):
    url = models.CharField(blank=False, null=True, max_length=200)
    account = models.ForeignKey("account_mapping.AccountMapping", null=True, blank=False,
                                on_delete=models.SET_NULL, related_name="mandators")
