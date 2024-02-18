from django.core.validators import RegexValidator
from django.db import models

class TimeStamp(models.Model):
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)
    is_active = models.BooleanField("Active", default=True)
    
    class Meta:
        abstract = True

class Contact(models.Model):
    city = models.CharField('City', max_length=200, blank=True, null=True)
    area = models.CharField('Area', max_length=200, blank=True, null=True)
    address = models.CharField('Adress', max_length=200, blank=True, null=True)
    zipcode = models.CharField('Postal Code',
                               max_length=5,
                               blank=True,
                               null=True,
                               validators=[
                                    RegexValidator(
                                        regex=r'^\d{5}$',
                                        message="Zipcode must be 5 digits."
                                    )])
    TIN_agency = models.CharField("Tax Authority", max_length=120, blank=True,
                                   null=True)
    phone = models.CharField('Phone', max_length=10,
                             blank=True, null=True,
                             validators=[
                                RegexValidator(
                                    regex=r'^\d{10}$',
                                    message="Phone number must be entered as 10"
                                            " digits.No other punctuation required."
                                )])
    email = models.CharField('Email',max_length=200,
                             blank=True, null=True,
                             validators=[
                                    RegexValidator(
                                        regex=r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+'
                                              r'@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+',
                                        message="Wrong email Format."
                                    )])
    
    class Meta:
        abstract = True

# class Note(models.Model):
#     note = models.CharField(max_length=220)