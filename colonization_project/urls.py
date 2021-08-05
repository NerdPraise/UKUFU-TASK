from django.urls import path

from .views import CompanyGetAPIView, PersonGetAPIView

urlpatterns = [
    path('person/', PersonGetAPIView.as_view(), name="user-get-view"),
    path('company/<int:pk>/', CompanyGetAPIView.as_view(), name="company-get-view"),
]
