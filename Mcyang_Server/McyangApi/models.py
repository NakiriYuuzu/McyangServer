from django.db import models


# Create your models here.
class Course(models.Model):
    courseID = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=100)

    def __str__(self):
        return self

    class Meta:
        db_table = "Z_Course"


class Teacher(models.Model):
    teacherID = models.AutoField(primary_key=True)
    course_ID = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacherName = models.CharField(max_length=100)

    def __str__(self):
        return self

    class Meta:
        db_table = "Z_Teacher"


class Student(models.Model):
    StudentID = models.AutoField(primary_key=True)
    StudentName = models.CharField(max_length=100)
    Course_ID = models.ManyToManyField(Course)

    def __str__(self):
        return self

    class Meta:
        db_table = "Z_Student"


class Sign(models.Model):
    signID = models.AutoField(primary_key=True)
    course_ID = models.IntegerField()
    student_ID = models.IntegerField()
    student_Name = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self

    class Meta:
        db_table = "Z_Sign"
