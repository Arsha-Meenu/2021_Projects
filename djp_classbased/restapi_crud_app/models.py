from django.db import models

# Create your models here.
class StudentsClass(models.Model):
    name = models.CharField(max_length = 255)
    dateofjoining = models.DateTimeField()

    def __str__(self):
        return self.name

    # def __iter__(self):
    #     return  iter('self.name','self.dateofjoining')
