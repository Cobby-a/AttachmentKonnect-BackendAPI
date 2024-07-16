from rest_framework import serializers
from .models import Manager, RoleDetail

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "companyName",
            "email",
            "password",
            "ceo",
            "location",
            "durationOfExistence",
            "briefInfo",
            "contractStatus",
            "reportStatus",
        )
        model = Manager

class RoleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "company",
            "role",
            "numberOfInterns",
            "deadline",
        )
        model = RoleDetail