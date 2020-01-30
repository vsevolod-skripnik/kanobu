from rest_framework import serializers

from opinions.models import Opinion


class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opinion
        fields = [
            'id',
            'category',
            'object_id',
            'content_type',
        ]
