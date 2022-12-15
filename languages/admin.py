from django.contrib import admin

from languages.models import Language, Word, Expression


admin.site.register(Language)
admin.site.register(Word)
admin.site.register(Expression)
