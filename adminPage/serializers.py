from rest_framework import serializers
from .models import AdminUser


class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'username',
            'password',
        )
        model = AdminUser