from rest_framework import serializers
from .models import Student, StudentRolesApplied

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "student_id",
            "password",
            "last_name",
            "other_names",
            "email",
            "phone_number",
            "profile_pic",
        )
        model = Student

class StudentRolesAppliedSerilaizer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            "student",
            "role",
            "applicationFile",
            "approval",
        )
        model = StudentRolesApplied

class StudentRolesAppliedSerilaizer1(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            "student",
            "role",
            "applicationFile",
            "approval",
        )
        model = StudentRolesApplied
        depth = 2