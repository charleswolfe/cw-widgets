from rest_framework import serializers

from .models import Widget


class WidgetSerializer(serializers.Serializer):
    id: int = serializers.IntegerField(read_only=True)
    name: str = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=64
    )
    number_of_parts: int = serializers.IntegerField()
    created = serializers.DateTimeField(required=False)
    updated = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        return Widget.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.number_of_parts = validated_data.get(
            'number_of_parts',
            instance.number_of_parts
        )
        instance.save()
        return instance
