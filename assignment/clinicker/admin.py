from django.contrib import admin
from .models import Doctor, Staffs, Assignments, SpecializationDB
# Register your models here.

admin.site.register(Doctor)
admin.site.register(Staffs)
admin.site.register(Assignments)
admin.site.register(SpecializationDB)
