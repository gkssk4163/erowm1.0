from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.xmlTest, name='xmlTst'),
    url(r'^monthly_report$', views.monthly_report, name='monthly_report'),
    url(r'^show_record$', views.show_record, name='show_record'),
    url(r'^budget_report$', views.budget_report, name='budget_report'),
    url(r'^settlement_report$', views.settlement_report, name='settlement_report'),
]
