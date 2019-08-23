from account_mapping.models import AccountMapping, Mandator
from rest_framework import serializers
from django.db import transaction


class MandatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mandator
        fields = ("id", "company_title", "url", "theme", "logo_url")

    @transaction.atomic
    def save(self, **kwargs):
        self.instance = super().save(**kwargs)
        return self.instance

    def save_mandator(self, instance):
        self.instance = instance
        return self.instance


class AccountMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountMapping
        fields = ("id", "email", "mandators", )

    mandators = MandatorSerializer(read_only=True, many=True)

    @transaction.atomic
    def save(self, mandator, **kwargs):
        self.instance = super().save(**kwargs)
        self.instance.mandators.add(mandator)
        return self.instance
