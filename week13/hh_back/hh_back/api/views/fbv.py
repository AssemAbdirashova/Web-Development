from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Company
from api.models import Vacancy
from api.serializer import CompanySerializer2
from api.serializer import VacancySerializer


@api_view(['GET', 'POST'])
def vacancy_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # return Response({'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({'key': 'value'}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST', 'PUT', 'DElETE'])
def vacancy_detailed(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Company.DoesNotExist as e:
        return Response({'error': str(e)})
    if request.method == 'GET':
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = VacancySerializer(instance=vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'DELETE':
        vacancy.delete()
        return Response({'deleted': True})


@api_view(['GET'])
def vacancy_companyID(request, company_id):
    if request.method == 'GET':
        vacancies = Vacancy.objects.filter(company_id=company_id)
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)
