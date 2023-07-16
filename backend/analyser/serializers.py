from rest_framework import serializers
from .models import Institutes,Branch

class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institutes
        fields = '__all__'

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'