from rest_framework import serializers
from .models import *


class FamilySerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomerFamily
		fields = ('id', 'family', 'relation', 'name', 'email', 'mobile', 'age', 'profession')

class CustomerSerializer(serializers.ModelSerializer):
	family = FamilySerializer(many=True, read_only=True)
	class Meta:
		model = Customer
		fields = ('id', 'name', 'email', 'mobile', 'age', 'profession','family')
