from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from account_mapping.models import AccountMapping, Mandator
from account_mapping.serializers import AccountMappingSerializer, MandatorSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers


class AccountMappingViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    serializer_class = AccountMappingSerializer
    queryset = AccountMapping.objects.all()
    pagination_class = PageNumberPagination

    def get_queryset(self):
        if "email" in self.request.GET:
            email = self.request.GET.get("email")
            self.queryset = self.queryset.filter(email__iexact=email)
        return self.queryset

    @transaction.atomic
    @action(detail=False, methods=['post'], url_name="submit-account", name="submit-account")
    def submit_account(self, request):
        serializer = AccountMappingSerializer(data=request.data)
        email = request.data.get("email")
        url = request.data.get("url")

        url_occurence = AccountMapping.objects.filter(mandators__url__iexact=url, email=email).distinct().count()
        if url_occurence > 0:
            raise serializers.ValidationError("URL für den Account schon vorhanden")

        mandator = Mandator.objects.filter(url__iexact=url).first()

        if not mandator:
            mandator = Mandator.objects.create(url=url)

        if serializer.is_valid():
            serializer.save(mandator=mandator)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MandatorViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin,
                      mixins.UpdateModelMixin, GenericViewSet):
    serializer_class = MandatorSerializer
    queryset = Mandator.objects.all()
    pagination_class = PageNumberPagination

    @action(detail=False, methods=['post'], url_name="submission", name="submission")
    def submission(self, request):
        serializer = MandatorSerializer(data=request.data)
        if serializer.is_valid():
            url = request.data.get("url")
            mandator = Mandator.objects.filter(url__iexact=url).first()
            if mandator:
                serializer.update(mandator, serializer.validated_data)
            else:
                serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
