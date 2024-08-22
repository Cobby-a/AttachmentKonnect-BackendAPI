from rest_framework import serializers
from .models import Supervisor, SupervisorNotification

class SupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "staff_id",
            "password",
            "last_name",
            "other_names",
            "profile_pic",
        )
        model = Supervisor

class SupervisorNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            # "supervisor",
            "notText",
        )
        model = SupervisorNotification

class SupervisorNotificationSerializer1(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            # "supervisor",
            "notText",
        )
        model = SupervisorNotification
        depth = 1