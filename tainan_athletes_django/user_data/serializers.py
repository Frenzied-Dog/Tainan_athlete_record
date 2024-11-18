from rest_framework import serializers
from .models import Athlete, Coach


class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields = '__all__'  # 包括所有字段


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = '__all__'  # 包括所有字段