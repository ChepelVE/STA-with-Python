from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        abstract = True


class Student(Person):
    pass

    class Meta:
        db_table = 'students'


class Teacher(Person):
    pass

    class Meta:
        db_table = 'teachers'


class Homework(models.Model):
    text = models.CharField(max_length=100)
    deadline = models.IntegerField()
    created = models.DateTimeField()

    class Meta:
        db_table = 'homeworks'


class HomeworkResult(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    solution = models.CharField(max_length=200)
    created = models.DateTimeField()

    class Meta:
        db_table = 'homework_results'



