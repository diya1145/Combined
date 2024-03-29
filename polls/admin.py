from django.contrib import admin
from .models import Choice, Question

from .models import Question

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    # prepopulated_fields = {'slug': ("question_text",)}
    


admin.site.register(Question, QuestionAdmin)
