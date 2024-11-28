from rest_framework import serializers
from .models import UserProfile


class ProfileSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField()
    thumbnail = serializers.ImageField()
    
    class Meta:
        model = UserProfile
        fields = '__all__'  # 包括所有字段