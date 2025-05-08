from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(allow_blank=True, required=False)
    completed = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Task(**validated_data).save() or Task.objects.get(**validated_data)
