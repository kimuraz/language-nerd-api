from rest_framework.viewsets import ReadOnlyModelViewSet\

from languages.serializers import LanguageSerializer, WordSerializer
from languages.models import Language, Word


class LanguageViewSet(ReadOnlyModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class WordViewSet(ReadOnlyModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
