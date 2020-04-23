from rest_framework import serializers

from api.models import Company, Vacancy


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    city = serializers.CharField()
    address = serializers.CharField()

    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'city', 'address')

    def create(self, validated_data):
        company = Company()
        company.name = validated_data.get('name')
        company.description = validated_data.get('description')
        company.city = validated_data.get('city')
        company.address = validated_data.get('address')

        company.save()
        return company

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.description = validated_data.get('description')
        instance.city = validated_data.get('city')
        instance.address = validated_data.get('address')

        instance.save()
        return instance


class CompanySerializer2(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'city', 'address')


class VacancySerializer(serializers.ModelSerializer):
    company_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Vacancy
        fields = ('id', 'name', 'description', 'salary', 'company_id')

    def create(self, validated_data):
        vacancy = Vacancy()
        vacancy.name = validated_data.get('name')
        vacancy.description = validated_data.get('description')
        vacancy.salary = validated_data.get('salary')
        vacancy.company_id = validated_data.get('company_id')

        vacancy.save()
        return vacancy

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.description = validated_data.get('description')
        instance.salary = validated_data.get('salary')
        instance.company_id_id = validated_data.get('company_id')

        instance.save()
        return instance


class CompanyWithVacanciesSerializer(serializers.ModelSerializer):
    # products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # products = serializers.StringRelatedField(many=True, read_only=True)
    vacancies = VacancySerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ('id', 'name', 'products')
