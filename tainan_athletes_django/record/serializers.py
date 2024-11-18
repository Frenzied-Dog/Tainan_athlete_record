from rest_framework import serializers
from .models import DailyTrainRecord, RaceRecord, HurtRecord


class DailyTrainRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyTrainRecord
        fields = '__all__'  # 包括所有字段


class RaceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaceRecord
        fields = '__all__'  # 包括所有字段


class HurtRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HurtRecord
        fields = '__all__'  # 包括所有字段
