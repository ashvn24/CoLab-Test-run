# urls.py
from django.urls import path
from .views import VideoUploadView

urlpatterns = [
    path('upload/', VideoUploadView.as_view(), name='video-upload'),
    # Add other URLs as needed
]
