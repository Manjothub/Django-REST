from django.contrib import admin
from .models import *


class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','type')
    search_fields=('name',)

admin.site.register(Company,CompanyAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','email','company')
    list_filter=('company',)
    
admin.site.register(Employee,EmployeeAdmin)