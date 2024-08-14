from rest_framework import serializers
from .models import Student, StudentRolesApplied, StudentAppliedInternship, StudentInternships, StudentNotification

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
    
class StudentSerializer1(serializers.ModelSerializer):
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
        depth = 1

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
        model = StudentAppliedInternship

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
        model = StudentAppliedInternship
        depth = 2
    
class StudentInternshipsSerilaizer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            "student",
            "role",
            "offer",
        )
        model = StudentInternships

class StudentInternshipsSerilaizer1(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            "student",
            "role",
            "offer",
        )
        model = StudentInternships
        depth = 2

class StudentNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "student",
            "notText",
        )
        model = StudentNotification

class StudentNotificationSerializer1(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "student",
            "notText",
        )
        model = StudentNotification
        depth = 1