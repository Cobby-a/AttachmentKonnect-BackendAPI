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
            "companyLogo"
        )
        model = Manager

class RoleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "company",
            "role",
            "numberOfInterns",
            "deadline",
            "moreInfo"
        )
        model = RoleDetail