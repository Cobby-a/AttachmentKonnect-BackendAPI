from rest_framework import serializers
from .models import Manager, RoleDetail, ManagerNotification, ManagerProfileChange, CompanyRegistered

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
            "website",
            "facebook",
            "twitter",
            "instagram",
            "companyLogo",
            "companyCertificate",
            "company_vacancies"
        )
        model = Manager
        # depth = 1

class CompanyRegisteredSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "companyName",
            "email",
        )
        model = CompanyRegistered

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

class ManagerChangeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "companyName",
            "email",
            "ceo",
            "location",
            "durationOfExistence",
            "briefInfo",
            "website",
            "facebook",
            "twitter",
            "instagram",
            "companyLogo",
        )
        model = ManagerProfileChange