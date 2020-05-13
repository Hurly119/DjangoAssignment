from django.db import models

# Create your models here.
class SpecializationDB(models.Model):
    specializationData = models.CharField(max_length=64)

    def __str__(self):
        return f"{ self.specializationData }"
class Doctor(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    specialized = models.ForeignKey(SpecializationDB, on_delete=models.CASCADE, related_name="specialization")

    def __str__(self):
        return f"{ self.last }, { self.first }"


class Staffs(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)

    def __str__(self):
        return f"{ self.last }, { self.first }"

class Assignments(models.Model):
    dateAssignment = models.DateField()
    doctorsAssigned = models.ManyToManyField(Doctor,blank=True,related_name="Doctors_assigned")
    staffAssigned = models.ManyToManyField(Staffs,blank=True,related_name="Staffs_assigned")

    def __str__(self):
        return f"{ self.dateAssignment }"
