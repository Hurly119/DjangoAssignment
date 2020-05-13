from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Doctor, Staffs, Assignments, SpecializationDB
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, "clinicker/index.html")

def doctors(request):
    context = {
    "doctors":Doctor.objects.all(),
    "specializations":SpecializationDB.objects.all()
    }
    return render(request, "clinicker/doctor.html",context)

def addDoctors(request):

    first = request.POST["firstName"]
    last = request.POST["lastName"]
    specs = int(request.POST["specialization"])
    if (not first or first.isspace()) or (not last or last.isspace()):
        messages.add_message(request, messages.ERROR, "Fields not filled.")
        return HttpResponseRedirect(reverse("doctors"))
    else:
        newDoctor = Doctor(first=first, last=last, specialized=SpecializationDB.objects.get(pk=specs))
        newDoctor.save()
        messages.add_message(request, messages.SUCCESS, "Doctor added successfully.")
        return HttpResponseRedirect(reverse("doctors"))

def removeDoctor(request, doctorID):
    doctorRemove = Doctor.objects.get(pk=doctorID)
    doctorRemove.delete()
    messages.add_message(request, messages.SUCCESS, "Doctor removed successfully.")
    return HttpResponseRedirect(reverse("doctors"))


def staffs(request):
    context = {
    "staffs":Staffs.objects.all()
    }
    return render(request, "clinicker/staff.html",context)

def addStaffs(request):
        first = request.POST["firstName"]
        last = request.POST["lastName"]
        if (not first or first.isspace()) or (not last or last.isspace()):
            messages.add_message(request, messages.ERROR, "Fields not filled.")
            return HttpResponseRedirect(reverse("staffs"))
        else:
            newStaff = Staffs(first=first, last=last)
            newStaff.save()
            messages.add_message(request, messages.SUCCESS, "Staff added successfully.")
            return HttpResponseRedirect(reverse("staffs"))

def removeStaff(request,staffID):
    staffRemove = Staffs.objects.get(pk=staffID)
    staffRemove.delete()
    messages.add_message(request, messages.SUCCESS, "Staff removed successfully.")
    return HttpResponseRedirect(reverse("staffs"))

def assignments(request):
    context = {
    "assignments":Assignments.objects.all()
    }
    return render(request, "clinicker/assignment.html",context)

def checkAssignment(request, assignmentID):
    AssignmentItem = Assignments.objects.get(pk=assignmentID)
    doctorObj = (AssignmentItem.doctorsAssigned.all())
    staffObj = (AssignmentItem.staffAssigned.all())
    doctorsAll = Doctor.objects.all()
    staffsAll = Staffs.objects.all()
    doctorsIn = []
    staffsIn = []
    for doctor in doctorsAll:
        if doctor not in doctorObj:
            doctorsIn.append(doctor)

    for staff in staffsAll:
        if staff not in staffObj:
            staffsIn.append(staff)

    context = {
    "assignment": Assignments.objects.get(pk=assignmentID),
    "DoctorsAvailable": doctorsIn,
    "StaffsAvailable": staffsIn,
    }
    return render(request, "clinicker/checkAssignment.html",context)

def assignAssignments(request, assignmentID):
    doctorID = int(request.POST["doctorsAvailable"])
    staffID = int(request.POST["staffsAvailable"])
    assignmentAdd = Assignments.objects.get(pk=assignmentID)
    if doctorID >= 0:
        doctorAdd = Doctor.objects.get(pk=doctorID)
        assignmentAdd.doctorsAssigned.add(doctorAdd)
    if staffID >= 0:
        staffAdd = Staffs.objects.get(pk=staffID)
        assignmentAdd.staffAssigned.add(staffAdd)
    return HttpResponseRedirect(reverse("checkAssignment",args=(assignmentID,)))

def removeAssignedDoctor(request,assignmentID,doctorID):
    doctorItem = Doctor.objects.get(pk=doctorID)
    assignmentItem = Assignments.objects.get(pk=assignmentID)
    assignmentItem.doctorsAssigned.remove(doctorItem)
    return HttpResponseRedirect(reverse("checkAssignment",args=(assignmentID,)))

def removeAssignedStaff(request,assignmentID,staffID):
    staffItem = Staffs.objects.get(pk=staffID)
    assignmentItem = Assignments.objects.get(pk=assignmentID)
    assignmentItem.staffAssigned.remove(staffItem)
    return HttpResponseRedirect(reverse("checkAssignment",args=(assignmentID,)))
