from django.db import models

# Create your models here.
class Topic_name(models.Model):
    Topics=models.CharField(max_length=100,primary_key=True)
class Student(models.Model):
    Name=models.CharField(max_length=100,primary_key=True)
    Age=models.IntegerField()
    Topics=models.ForeignKey(Topic_name,on_delete=models.CASCADE)
class List_student(models.Model):
    Roll_no=models.IntegerField(primary_key=True)
    Name=models.ForeignKey(Student,on_delete=models.CASCADE)
    Titls=models.CharField(max_length=200)
    Date=models.DateField()

