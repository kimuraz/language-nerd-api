from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response

from languages.serializers import LanguageSerializer, WordSerializer
from languages.models import Language, Word


class LanguageViewSet(ReadOnlyModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class WordViewSet(ReadOnlyModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    def list(self, request):
        languages = request.query_params.get('langs', None)
        if languages is not None:
            languages = languages.split(',')
            self.queryset = self.queryset.filter(language__code__in=languages)

        serializer = WordSerializer(self.queryset, many=True)
        return Response(serializer.data)
