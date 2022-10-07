from rest_framework import serializers

from api.models import Company, JobPost


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class JobPostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = '__all__'

class JobPostRetrieveSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name')
    country = serializers.CharField(source='company.country')
    city = serializers.CharField(source='company.city')

    class Meta:
        model = JobPost
        fields = ['id', 'company_name', 'country', 'city', 'position', 'compensation', 'stack', 'content']

class JobPostListSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name')
    country = serializers.CharField(source='company.country')
    city = serializers.CharField(source='company.city')

    class Meta:
        model = JobPost
        fields = ['id', 'company_name', 'country', 'city', 'position', 'compensation', 'stack']

class JobPostUpdateserializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = ['position', 'compensation', 'content', 'stack']


