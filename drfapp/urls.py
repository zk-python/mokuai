from django.urls import path

from drfapp import views

urlpatterns = [
    path("users/", views.UserAPIView.as_view()),
    path("computers/", views.ComputerAPIView.as_view()),
]
