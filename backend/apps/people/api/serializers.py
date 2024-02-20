from rest_framework import serializers

from ..models import Supplier

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            'company', 'person', 'TIN_agency','TIN_num',
            'city', 'area', 'address', 'zipcode', 'phone',
            'email', 'id'
        ]
        