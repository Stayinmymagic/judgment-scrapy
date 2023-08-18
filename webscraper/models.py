from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Judge(models.Model):
    pid =  models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    court = models.CharField(max_length=10)
    crime_type = models.CharField(max_length=10)
    event_time = models.DateTimeField()
    event_age =  models.IntegerField(default = 0)
    amount = models.CharField(default = 0,max_length=20)
    company = models.TextField(blank=True)
    map_family = models.CharField(max_length=10) # 是否配對到父母名
    map_address = models.CharField(max_length=10) # 是否配對到地址
    # ccis_company = models.CharField(max_length=10) # 是否配對到拒往備查公司名
    link = models.TextField(blank=True)
 
class Lender(models.Model):
    id =  models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=10)
    age = models.IntegerField(default = 0)
    fatherName = models.CharField(max_length = 10, blank=True, null=True)
    motherName = models.CharField(max_length = 10, blank=True, null=True)
    residenceAddress = models.TextField(null=True)
    companyAddress = models.TextField(null=True)
    currentAdddress = models.TextField(null=True)
    source = models.CharField(max_length = 10)



