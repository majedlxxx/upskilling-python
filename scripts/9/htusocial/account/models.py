from django.db import models

# Create your models here.

'''
CREATE TABLE Account(fname varchar(50), lname varchar(50), password varchar(100));
'''
class Account(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.fname + " " + self.lname

    
#Account.objects.all() => select * from account_account;

#Account.objects.filter(fname="majed") => select * from account where fname='majed';
#Account.objects.filter(fname="majed", password = '1234') =>  select * from account where fname='majed' and password='1234';
# Account(fname='majed', lname='lutfi', password='1234'); a.save() = > insert into account(fname, lname, password) values('majed', 'lutfi', '1234');
