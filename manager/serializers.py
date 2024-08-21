from rest_framework import serializers
from .models import Manager, RoleDetail, ManagerNotification

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
            "companyCertificate",
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
            "total_accepted_students",           
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
            "total_accepted_students",
        )
        model = RoleDetail
        depth = 2

class ManagerNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "company",
            "role",
            "notText",
        )
        model = ManagerNotification

class ManagerNotificationSerializer1(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "company",
            "role",
            "notText",
        )
        model = ManagerNotification
        depth = 1