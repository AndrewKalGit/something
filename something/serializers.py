
from rest_framework import serializers
from .models import Company, Cars


class CompanySerializer(serializers.HyperLinkedModelSerializer):
    cars = serializers.HyperLinkedRelatedField(
        view_name='car_detail', many=True, read_only=True
    )
    company_url = serializers.ModelSerializer.serializer_url_field(
        view_name='company_detail'
    )

    class Meta:
        fields = ('id', 'name', 'company_site',
                  'location', 'company_url', 'cars')


class CarsSerializer(serializers.HyperLinkedModelSerializer):
    companies = serializers.HyperLinkedRelatedField(
        view_name='company_detail', read_only=True
    )
    company_id = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(), source='Company'
    )

    class Meta:
        model = Cars
        fields = ('id', 'model', 'year', 'make', 'company_id', 'companies')
