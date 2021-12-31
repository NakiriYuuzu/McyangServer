from django.db import models


# Create your models here.

class Course(models.Model):
    id_course = models.AutoField(primary_key=True)
    name_course = models.CharField(max_length=100)

    def __str__(self):
        return self

    class Meta:
        db_table = 'A_course'


class Teacher(models.Model):
    id_teacher = models.AutoField(primary_key=True)
    name_teacher = models.CharField(max_length=100)
    id_course = models.ManyToManyField(Course, verbose_name="")

    def __str__(self):
        return self

    class Meta:
        db_table = 'A_teacher'


class Student(models.Model):
    id_student = models.AutoField(primary_key=True, auto_created=True)
    name_student = models.CharField(max_length=100)
    id_course = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return self

    class Meta:
        db_table = 'A_student'


class Sign(models.Model):
    id_sign = models.DateTimeField(auto_now_add=True, primary_key=True)
    id_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    id_student = models.ForeignKey(Student, on_delete=models.CASCADE)
    checked = models.BooleanField(default=True)

    def __str__(self):
        return self

    class Meta:
        db_table = 'A_sign'
