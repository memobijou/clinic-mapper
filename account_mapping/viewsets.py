from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from account_mapping.models import AccountMapping
from account_mapping.serializers import AccountMappingSerializer, MandatorSerializer
from rest_framework.pagination import PageNumberPagination


class AccountMappingViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    serializer_class = AccountMappingSerializer
    queryset = AccountMapping.objects.all()
    pagination_class = PageNumberPagination

    def get_queryset(self):
        if "email" in self.request.GET:
            email = self.request.GET.get("email")
            self.queryset = self.queryset.filter(email__iexact=email)
        return self.queryset

    @action(detail=False, methods=['post'], url_name="submit-account", name="submit-account")
    def submit_account(self, request):
        serializer = MandatorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(email=request.data.get("email"))
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
