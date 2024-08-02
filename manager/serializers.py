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
            "companyLogo",
            "company_vacancies"
        )
        model = Manager
        # depth = 1

class RoleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "company",
            "role",
            "numberOfInterns",
            "deadline",
            "moreInfo",            
        )
        model = RoleDetail

class RoleDetailSerializer1(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "company",
            "role",
            "numberOfInterns",
            "deadline",
            "moreInfo",
            'student_roles_applied',
        )
        model = RoleDetail
        depth = 2