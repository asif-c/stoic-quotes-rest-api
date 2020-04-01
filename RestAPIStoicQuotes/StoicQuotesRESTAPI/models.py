from __future__ import unicode_literals

from django.db import models



class StoicQuotes(models.Model):

    '''
    Following are the columns of the table
    '''

    philosophers_name=models.CharField(max_length=255)
    quotes=models.TextField()

