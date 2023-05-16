from django.urls import path
from vueOne import views

urlpatterns = [
   path('student/', views.StudentList.as_view()),
   path('student/<int:pk>/', views.StudentDetail.as_view()),
]