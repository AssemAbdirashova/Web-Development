from django.urls import path
from api.views.fbv import vacancy_detailed, vacancy_list, vacancy_companyID
#from api.views import company_list, company_by_id, company_vacancy, vacancy_list, vacancy_by_id, vacancy_top
from api.views.cbv import CompanyListAPIView, CompanyDetailAPIView
urlpatterns = [
    path('companies/', CompanyListAPIView.as_view()),
    path('companies/<int:company_id>/', CompanyDetailAPIView.as_view()),
    path('vacancies/', vacancy_list),
    path('vacancies/<int:vacancy_id>/', vacancy_detailed),
    path('companies/<int:company_id>/vacancies/', vacancy_companyID),


    # path('products/', ProductListAPIView.as_view()),
    # path('products/<int:pk>/', ProductDetailAPIView.as_view()),
    #
    #
    #
    # path('companies/', company_list),
    # path('companies/<int:company_id/>', company_by_id),
    # path('companies/<int:company_id>/vacancies/', company_vacancy),

    # path('vacancies/top_ten/', vacancy_top)
]