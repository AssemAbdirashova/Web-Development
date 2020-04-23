import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import Company
from api.models import Company, Vacancy
from django.http import Http404
from django.http.response import JsonResponse



def company_list(request):
    companies = Company.objects.all()
    companies_json = [company.to_json() for company in companies]
    return JsonResponse(companies_json, safe=False)

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)

def company_by_id(request, company_id):
    try:
        company = Company.objects.get(id = company_id)
    except Company.DoesNotExist as e:
        raise Http404
    return JsonResponse(company.to_json())

def vacancy_by_id(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id = vacancy_id)
    except Vacancy.DoesNotExist as e:
        raise Http404
    return JsonResponse(vacancy.to_json())

def company_vacancy(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    vacancies = company.vacancy_set.all()
    vacancies_json = [v.to_json() for v in vacancies]

    return JsonResponse(vacancies_json, safe=False)

def vacancy_top(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)



# CRUD - For Category Model

@csrf_exempt
def category_list(request):
    if request.method == 'GET':
        categories = Company.objects.all()
        categories_json = [c.to_json() for c in categories]
        return JsonResponse(categories_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)

        # option 1
        # category = Category(name=data['name'])
        # category.save()

        # option 2
        category = Company.objects.create(name=data.get('name'))

        return JsonResponse(category.to_json())


@csrf_exempt
def category_detail(request, category_id):
    try:
        category = Company.objects.get(id=category_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    # Get one objects
    if request.method == 'GET':
        return JsonResponse(category.to_json())

    # Update selected objects
    elif request.method == 'PUT':
        data = json.loads(request.body)

        category.name = data.get('name', category.name)
        category.save()

        return JsonResponse(category.to_json())

    # Delete selected object
    elif request.method == 'DELETE':
        category.delete()

        return JsonResponse({'deleted': True})