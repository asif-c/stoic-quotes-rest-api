from django.http import HttpResponse
from rest_framework import generics
from .models import StoicQuotes
from .serializers import StoicQuotesSerializer
import random

class StoicQuotesList(generics.ListAPIView):

    # queryset=StoicQuotes.objects.all()

    serializer_class=StoicQuotesSerializer

    def get_queryset(self):

        total_objects=StoicQuotes.objects.all().count()
        a_random_number=random.randint(1,total_objects)
        return StoicQuotes.objects.filter(pk=a_random_number)
