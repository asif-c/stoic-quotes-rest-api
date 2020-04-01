from .models import StoicQuotes
from rest_framework import serializers


class StoicQuotesSerializer(serializers.ModelSerializer):

    class Meta:
        model=StoicQuotes

        fields=['philosophers_name','quotes']