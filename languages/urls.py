from rest_framework.routers import SimpleRouter

from languages.views import LanguageViewSet, WordViewSet


router = SimpleRouter()
router.register(r'languages', LanguageViewSet)
router.register(r'words', WordViewSet)

url_patterns = router.urls
