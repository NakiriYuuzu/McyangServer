from django.urls import path
from .views import CourseApiView, CourseDetail, TeacherApiView, TeacherDetail, StudentApiView, StudentDetail, \
    SignApiView, SignDetail

urlpatterns = [
    # Course API
    path('api/course/', CourseApiView.as_view()),
    path('api/course/detail/<int:id>/', CourseDetail.as_view()),

    # Teacher API
    path('api/teacher/', TeacherApiView.as_view()),
    path('api/teacher/detail/<int:id>/', TeacherDetail.as_view()),

    # Student API
    path('api/student/', StudentApiView.as_view()),
    path('api/student/detail/<int:id>/', StudentDetail.as_view()),

    # Sign API
    path('api/sign/', SignApiView.as_view()),
    path('api/sign/detail/<int:id>/', SignDetail.as_view()),

    # QA API
]
