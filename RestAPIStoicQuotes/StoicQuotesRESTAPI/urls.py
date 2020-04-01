from django.urls import path
from . import views

app_name='StoicQuotesRESTAPI'

urlpatterns = [

    path('StoicQuotesRESTAPI/',views.StoicQuotesList.as_view())
]