from django.contrib import admin
from .models import Company, CompanyMembership, CompanyUpdate

admin.site.register(Company)
admin.site.register(CompanyMembership)
admin.site.register(CompanyUpdate)
