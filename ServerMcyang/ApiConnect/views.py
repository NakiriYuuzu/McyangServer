from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import CourseSerializer, TeacherSerializer, StudentSerializer, SignSerializer
from .models import Course, Teacher, Student, Sign


# CourseAPI
class CourseApiView(APIView):
    def get(self, request):
        self.as_view()
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)

    def post(self, request):
        self.as_view()
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetail(APIView):
    def get_object(self, id):
        self.as_view()
        try:
            return Course.objects.get(id_course=id)
        except Course.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        course = self.get_object(id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)


# Student API
class StudentApiView(APIView):
    def get(self, request):
        self.as_view()
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)

    def post(self, request):
        self.as_view()
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetail(APIView):
    def get_object(self, student_id):
        self.as_view()
        try:
            return Student.objects.get(id_student=student_id)
        except Student.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, student_id):
        student = self.get_object(student_id)
        serializer = CourseSerializer(student)
        return Response(serializer.data)


# Teacher
class TeacherApiView(APIView):
    def get(self, request):
        self.as_view()
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data)

    def post(self, request):
        self.as_view()
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherDetail(APIView):
    def get_object(self, teacher_id):
        self.as_view()
        try:
            return Teacher.objects.get(id_teacher=teacher_id)
        except Teacher.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, teacher_id):
        teacher = self.get_object(teacher_id)
        serializer = CourseSerializer(teacher)
        return Response(serializer.data)


# Sign
class SignApiView(APIView):
    def get(self, request):
        self.as_view()
        sign = Sign.objects.order_by('id_sign')
        serializer = SignSerializer(sign, many=True)
        return Response(serializer.data)

    def post(self, request):
        self.as_view()
        serializer = SignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignDetail(APIView):
    def get_object(self, sign_id):
        self.as_view()
        try:
            return Sign.objects.get(id_sign=sign_id)
        except Sign.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, sign_id):
        teacher = self.get_object(sign_id)
        serializer = SignSerializer(teacher)
        return Response(serializer.data)
