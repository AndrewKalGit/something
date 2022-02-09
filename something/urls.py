from django.urls import path
from . import views


urlpatterns = [
    path('companies/', views.CompanyList.as_view(), name='company_list'),
    path('companies/<int:pk>', views.CompanyDetail.as_view(), name='company_detail'),
    path('cars/', views.CarList.as_view(), name='car_list'),
    path('cars/<int:pk>', views.CarDetail.as_view(), name='car_detail')

]
