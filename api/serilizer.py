from rest_framework import serializers

from rest_framework import viewsets
from rest_framework import status

from . models import Knowledge_base



class KnowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Knowledge_base
        fields = '__all__'     