from rest_framework import serializers
from ..models import (PayeeLabel, Payee, Payment,
                      Source, Income)

class PayeeLabelSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='cashflow:payeelabel-item',
        lookup_field='id',
        )  
     
    class Meta:
        model = PayeeLabel
        fields = ['id', 'name', 'url']

class PayeeSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='cashflow:payee-item',
        lookup_field='id',
        ) 
    label = serializers.PrimaryKeyRelatedField(queryset=PayeeLabel.objects.all())
    label_name = serializers.SerializerMethodField()
    class Meta:
        model = Payee
        fields = ['id', 'name', 'label','label_name', 'summary', 'active', 'url']

    def get_label_name(self, obj):
        return obj.label.name 

class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='cashflow:payment-item',
        lookup_field='id',
        ) 
    payee = serializers.PrimaryKeyRelatedField(queryset=Payee.objects.all())
    payee_name = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = ['id', 'payee_name','payee', 'amount', 'url',
                  'payment_day', 'summary', 'paid' ]

    def get_payee_name(self, obj):
        return obj.payee.name 
    
    def validate_amount(self, amount):
        if amount < 0:
            raise serializers.ValidationError("Tax value cannot be negative.")
        return amount
    
class SourceSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='cashflow:source-item',
        lookup_field='id',
        ) 
    class Meta:
        model = Source
        fields = ['id', 'source', 'summary', 'url']

    

class IncomeSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='cashflow:income-item',
        lookup_field='id',
        ) 
    source = serializers.PrimaryKeyRelatedField(queryset=Source.objects.all())
    source_name = serializers.SerializerMethodField()

    class Meta:
        model = Income
        fields = ['id','source_name', 'source', 'amount',
                  'summary', 'income_date', 'url']

    def get_source_name(self,obj):
        return obj.source.source
    
    def validate_amount(self, amount):
        if amount < 0:
            raise serializers.ValidationError("Tax value cannot be negative.")
        return amount