from rest_framework.routers import SimpleRouter

from training.views import FlashcardViewSet

router = SimpleRouter()
router.register(r'flashcards', FlashcardViewSet)

url_patterns = router.urls
