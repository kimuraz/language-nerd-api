from django.db import models

from languages.models import Language, Word


class Flashcard(models.Model):
    observation = models.TextField(null=True, blank=True)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.word.word
