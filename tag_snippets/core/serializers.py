from rest_framework import serializers
from .models import TagModel, SnippetModel


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagModel
        fields = '__all__'

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnippetModel
        fields = '__all__'

