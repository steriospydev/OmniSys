import uuid
from django.core.validators import RegexValidator
from django.db import models

from apps.tools.models import TimeStamp, Contact

class Supplier(TimeStamp, Contact):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          db_index=True,
                          editable=False)
    company = models.CharField("Company", max_length=120, unique=True)
    person = models.CharField("Representative", max_length=120,
                               blank=True, null=True)  
    TIN_agency = models.CharField("Tax Authority", max_length=120, blank=True,
                                   null=True)
    TIN_num = models.CharField("Tax number",
                               max_length=9,
                               validators=[
                                   RegexValidator(
                                       regex=r"^[0-9]{9}$",
                                       message="Invalid Greek TIN number. It must contain 9 digits."
                                   )],
                               unique=True)
    
    
    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'

    def __str__(self):
        return f'{self.company}'