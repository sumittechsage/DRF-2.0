from django.shortcuts import render
from django.http import JsonResponse
from .models import Student
# Create your views here.
def list_student_records(request):
    student_data_1 = Student.vidhyarthi.all()  # vidhyarhi is student model manager name
    student_data_2 = Student.students.all()  # students is another student model manager name
    student_data_3 = Student.students.get_stu_roll_range(3,9)  # students is another student model manager name
    print("student data 1 ====>", student_data_1)
    print("student data 2 ====>", student_data_2)
    print("student data 3 ====>", student_data_3)
    return JsonResponse({"message" : "request successful"}, status = 200)


