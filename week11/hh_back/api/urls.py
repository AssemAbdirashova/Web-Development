from django.urls import path
from api.views import company_list, company_by_id, company_vacancy, vacancy_list, vacancy_by_id, vacancy_top

urlpatterns = [
    path('companies/', company_list),
    path('companies/<int:company_id/>', company_by_id),
    path('companies/<int:company_id>/vacancies/', company_vacancy),
    path('vacancies/', vacancy_list),
    path('vacancies/<int:vacancy_id>/', vacancy_by_id),
    path('vacancies/top_ten/', vacancy_top)


]