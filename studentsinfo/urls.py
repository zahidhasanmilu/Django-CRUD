from django.urls import path
from .import views

urlpatterns = [
    path('', views.allstudent , name="allstudent"),
    path('addstudent/', views.addstudent, name="addstudent"),
    path('update/<int:id>', views.update, name="update"),
    path('delete_student/<int:id>', views.delete_student, name="delete_student"),
]