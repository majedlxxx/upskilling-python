from django.db import models
from account.models import Account

class Post(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE) 
    # CASCADE vs SET_NULL
    '''
        CASCADE: when the author is deleted all his posts will be deleted.
        SET_NULL: when the author is deleted all his posts will have their author set to null.
    '''
    title = models.CharField(max_length=100)
    content = models.TextField()
    