from django.contrib import admin
from .models import About, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin



@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    list_display = ('author', 'content', 'updated_on')
    summernote_fields = ('content',)

@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)

# Register your models here.
    

