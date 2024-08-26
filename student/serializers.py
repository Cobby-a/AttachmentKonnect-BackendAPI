from rest_framework import serializers
from .models import Student, StudentRolesApplied, StudentAppliedInternship, StudentInternships, StudentNotification, StudentAssessment

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
            "company",
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
            "company",
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
            "company",
            "offer",
        )
        model = StudentInternships

class StudentInternshipsSerilaizer1(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            "student",
            "role",
            "company",
            "offer",
        )
        model = StudentInternships
        depth = 2

class ManagerStudentInternshipsSerilaizer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            "student",
            "role",
            "company",
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

class StudentInternAssessmentSerializer(serializers.ModelSerializer):
    student_last_name = serializers.CharField(source='student.last_name', read_only=True)
    student_other_names = serializers.CharField(source='student.other_names', read_only=True)
    company_name = serializers.CharField(source='company.companyName', read_only=True)
    class Meta:
        fields = (
            "student",
            "student_last_name",
            "student_other_names",
            "company",
            "company_name",
            "email",
            "durationOfInternship",
            "qualityOfWork",
            "abilityToWork",
            "initiativeAndCreativity",
            "characterTraits",
            "dependabilty",
            "attendanceAndPunctuality",
            "organizationalFit",
            "responseToSupervision",
            "suggestionsForImprovement",
            "nameOfSupervisor",
            "positionOfSupervisor",
            "supervisorEmail",
            "supervisorContact",
        )
        model = StudentAssessment

class StudentInternAssessmentSerializer1(serializers.ModelSerializer):
    student = StudentSerializer()
    class Meta:
        fields = (
            "student",
            "company",
            "email",
            "durationOfInternship",
            "qualityOfWork",
            "abilityToWork",
            "initiativeAndCreativity",
            "characterTraits",
            "dependabilty",
            "attendanceAndPunctuality",
            "organizationalFit",
            "responseToSupervision",
            "suggestionsForImprovement",
            "nameOfSupervisor",
            "positionOfSupervisor",
            "supervisorEmail",
            "supervisorContact",
        )
        model = StudentAssessment
        depth = 1