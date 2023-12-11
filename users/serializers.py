from rest_framework import serializers

from .models import UserError


class UserErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserError
        fields = "__all__"
