from django.contrib import admin

from .models import (PayeeLabel, Payee, Payment,
                     Source, Income)

@admin.site.register(Payee)
class PayeeAdmin(admin.ModelAdmin):
    model = Payee
    list_display = ('name','label', 'active')
    list_editable = ('active')

@admin.site.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    model = Payment
    list_display = ('payee','amount', 'payment_day','paid')
    list_editable = ('paid', 'payment_day')
    
@admin.site.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    model = Income
    list_display = ('source','amount','income_date')
    list_editable = ('amount', 'income_date')

admin.site.register(PayeeLabel)
admin.site.register(Source)