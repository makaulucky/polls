from django.contrib import admin
from .models import Question, Choice
from django.urls import reverse


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.site_header = "Admin | Insquare Technologies ~ Polls"
admin.site.site_title = "Insquare Admin"
admin.site.index_title = "Welcome to Insquare Technologies ~ Polls"

