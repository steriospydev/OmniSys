import uuid
from django.db import models
from django.utils import timezone

from apps.tools.models import TimeStamp, AmountValidation

class PayeeLabel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            db_index=True, editable=False)   
    name = models.CharField(max_length=30, unique=True)

    def __str__(self) -> str:
        return f'{self.name}'

class Payee(TimeStamp):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          db_index=True, editable=False)
    label = models.ForeignKey(PayeeLabel, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=40)
    summary = models.CharField(max_length=200, blank=True, null=True)
    active = models.BooleanField(default=True)


    class Meta:
        unique_together = ['label', 'name']

    def __str__(self) -> str:
        return f'{self.name}-{self.label}'    

class Payment(TimeStamp, AmountValidation):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          db_index=True, editable=False)
    payee = models.ForeignKey(Payee, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    summary = models.CharField(max_length=200, blank=True, null=True)
    payment_day = models.DateTimeField(blank=True, null=True,
                                       default=timezone.now)
    paid = models.BooleanField(default=True)

    class Meta:
        ordering = ['paid', '-payment_day']

    def __str__(self):
        return f'{self.payee.name} - {self.created_at.strftime("%b %d %Y")}'
    

class Source(TimeStamp):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, 
                          db_index=True, editable=False)
    source = models.CharField(max_length=40, unique=True)
    summary = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.source}'

    
class Income(TimeStamp, AmountValidation):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          db_index=True, editable=False)
    source = models.ForeignKey(Source, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    summary = models.CharField(max_length=200, blank=True, null=True)
    income_date =models.DateTimeField(blank=True, null=True, default=timezone.now)
      
    def __str__(self) -> str:
        return f'{self.source} - {self.amount}'
    