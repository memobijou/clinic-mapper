from account_mapping.models import AccountMapping, Mandator
from rest_framework import serializers
from django.db import transaction


class MandatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mandator
        fields = ("id", "title", "url", "theme", "logo_url")

    @transaction.atomic
    def save(self, email, **kwargs):
        self.instance = super().save(**kwargs)
        account = AccountMapping.objects.filter(email__icontains=email).first()
        if not account:
            account = AccountMapping.objects.create(email=email)

        self.instance.account = account
        url = self.instance.url
        url_occurence = Mandator.objects.filter(url__iexact=url, account__email=email).count()
        if url_occurence > 0:
            raise serializers.ValidationError("URL für den Account schon vorhanden")
        self.instance.save()
        return self.instance


class AccountMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountMapping
        fields = ("id", "email", "mandators", )

    mandators = MandatorSerializer(read_only=True, many=True)
