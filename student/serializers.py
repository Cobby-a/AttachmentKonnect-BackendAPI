from rest_framework import serializers
from .models import Student, StudentRolesApplied, StudentInternship

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
            "level",
            "programme",
        )
        model = Student

class StudentRolesAppliedSerilaizer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            "student",
            "role",
            "applicationFile",
            "applicationDate",
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
            "applicationDate",
            "approval",
        )
        model = StudentRolesApplied
        depth = 2

class StudentInternshipSerilaizer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            "student",
            "role",
            "approval",
            "smallInfo",
            "start_date",
            "end_data",
            "optionalFile",
        )
        model = StudentInternship

class StudentInternshipSerilaizer1(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            "student",
            "role",
            "approval",
            "smallInfo",
            "start_date",
            "end_data",
            "optionalFile",
        )
        model = StudentInternship
        depth = 2