from django.contrib import admin
from .models import UploadedFile




class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'hash', 'uploaded_at')  # Display in admin panel
    search_fields = ('hash', 'file')  # Allow searching
    ordering = ('-uploaded_at',)  # Show newest first

admin.site.register(UploadedFile, UploadedFileAdmin)