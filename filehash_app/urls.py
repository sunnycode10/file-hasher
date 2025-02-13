from .views import upload_file
from django.urls import path

urlpatterns = [
    path('', upload_file, name='upload_file'),
]