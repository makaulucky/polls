# polls/admin.py

from django.contrib import admin
from django.utils import timezone
import datetime
from .models import Question, Choice

admin.site.site_header = "Admin | Insquare Technologies ~ Polls"
admin.site.site_title = "Insquare Admin"
admin.site.index_title = "Welcome to Insquare Technologies ~ Polls"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently', 'total_votes')
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self, obj):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= obj.pub_date <= now

    def total_votes(self, obj):
        return sum(choice.votes for choice in obj.choice_set.all())

    total_votes.short_description = "Total Votes"


admin.site.register(Question, QuestionAdmin)
