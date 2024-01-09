from django.contrib import admin
from django.urls import path,include
from  .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies',CompanyViewSet)
router.register(r'employees',EmployeeViewSet)


urlpatterns = [
    path('',include(router.urls))
]