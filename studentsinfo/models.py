from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Section(models.Model):
    name = models.CharField(max_length=5)
    
    
    def __str__(self):
        return self.name

class Semester(models.Model):
    name = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
    

class Student(models.Model):
    name = models.CharField(max_length=20)
    student_id = models.IntegerField(default=0, blank=False, null=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    section = models.ForeignKey(Section,on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
    