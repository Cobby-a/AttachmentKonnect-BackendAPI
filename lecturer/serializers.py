from rest_framework import serializers
from .models import Lecture

class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "staff_id",
            "password",
            "last_name",
            "other_names",
        )
        model = Lecture