from django.urls import path
from .views import EmployeeCBV


urlpatterns = [
    path('', EmployeeCBV.as_view())
]
