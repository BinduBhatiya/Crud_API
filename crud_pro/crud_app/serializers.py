from rest_framework import serializers
from .models import studentmodel

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model = studentmodel
        fields = '__all__'