import logging
from rest_framework.viewsets import ModelReadOnlyViewSet
from rest_framework.response import Response

from training.models import Flashcard
from training.serializers import FlashcardSerializer


class FlashcardViewSet(ModelReadOnlyViewSet):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer

    def list(self, request):
        languages = request.query_params.get('langs', None)
        if languages is not None:
            languages = languages.split(',')
            self.queryset = self.queryset.filter(language__code__in=languages)
        try:
            num_cards = int(request.query_params.get('cards', 10))
        except ValueError as e:
            num_cards = 10

        queryset = self.queryset.order_by('?')[:num_cards]
        serializer = FlashcardSerializer(queryset, many=True)
        return Response(serializer.data)
