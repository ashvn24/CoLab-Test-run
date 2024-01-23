# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Video
from .serializers import VideoSerializer
import os
from googleapiclient.http import MediaFileUpload
from .youtube_utils import get_authenticated_service

from myyoutubeproject.settings import OWNER_SECRET_FILE_PATH

class VideoUploadView(APIView):
    def post(self, request, *args, **kwargs):
        # Assuming video file is included in the request data
        video_file = request.data.get('video_file')
        
        # Validate other required fields
        serializer = VideoSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Save video info to database
        video_instance = serializer.save()

        # Upload video to YouTube
        video_id = self.upload_to_youtube(video_instance)

        if video_id:
            return Response({'video_id': video_id}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Failed to upload video'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def upload_to_youtube(self, video_instance):
        youtube = get_authenticated_service("./owner_credentials.json")  # Use owner's credentials

        request_body = {
            'snippet': {
                'title': video_instance.title,
                'description': video_instance.description,
            },
            'status': {
                'privacyStatus': video_instance.privacy_status,
            },
        }

        media_file_upload = MediaFileUpload(video_instance.video_path.path, chunksize=-1, resumable=True)

        try:
            videos_insert_response = youtube.videos().insert(
                part='snippet,status',
                body=request_body,
                media_body=media_file_upload
            ).execute()

            video_id = videos_insert_response['id']
            
            if video_id:
                os.remove("./owner_credentials.json")

            return video_id

        except Exception as e:
            print(f"Error uploading video: {e}")
            return None
