from django.urls import path
from . import views
urlpatterns = [
      path("", views.index, name="index"),
      path("staffs", views.staffs, name="staffs"),
      path("staffs/add", views.addStaffs, name="addStaffs"),
      path("staffs/remove/<int:staffID>", views.removeStaff, name="removeStaff"),
      path("assignments", views.assignments, name="assignments"),
      path("assignments/<int:assignmentID>",views.checkAssignment, name="checkAssignment"),
      path("assignments/<int:assignmentID>/doctor/<int:doctorID>",views.removeAssignedDoctor,name="removeAssignedDoctor"),
      path("assignments/<int:assignmentID>/staff/<int:staffID>",views.removeAssignedStaff,name="removeAssignedStaff"),
      path("assignments/<int:assignmentID>/add", views.assignAssignments,name="assignAssignments"),
      path("doctors", views.doctors, name="doctors"),
      path("doctors/add", views.addDoctors, name="addDoctors"),
      path("doctors/remove/<int:doctorID>",views.removeDoctor, name="removeDoctor")
      ]
