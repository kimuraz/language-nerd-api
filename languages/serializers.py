from rest_framework import serializers
from languages.models import Language, Word


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name', 'code')


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'
