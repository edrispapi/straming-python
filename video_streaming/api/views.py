"""API Views for Courses, Streams, and Archives"""
from rest_framework import generics, permissions
from .serializers import CourseSerializer, VideoSerializer
from .models import Course, Video

class CourseListAPIView(generics.ListCreateAPIView):
    """لیست و ثبت دوره‌ها"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

class VideoDetailAPIView(generics.RetrieveAPIView):
    """دریافت جزئیات ویدئو (ویدئو آرشیو)"""
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]
