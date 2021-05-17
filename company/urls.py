from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('msci-data-analytics/', views.msci_data_analytics, name='msci_data_analytics'),
    path('sp-data-analytics/', views.sp_data_analytics, name='sp_data_analytics'),
    path('esg-score/', views.esg_score, name='esg_score'),
    path('<str:company_name>/', views.detail, name='detail'),
]
