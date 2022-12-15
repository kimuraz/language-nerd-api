from rest_framework.serializers import ModelSerializer

from training.models import Flashcard
from languages.serializers import WordSerializer


class FlashcardSerializer(ModelSerializer):
    word = WordSerializer()

    class Meta:
        model = Flashcard
        fields = '__all__'
