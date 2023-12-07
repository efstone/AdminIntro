from django.contrib import admin
from mp_admin_fun.models import Developer, Company


class DeveloperInline(admin.TabularInline):
    model = Developer
    readonly_fields = ['first_name', 'last_name', 'email', 'phone', 'street_address', 'city', 'state', 'zip_code', 'company']


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'search_with_google', 'company']
    list_filter = ['state', 'company']
    search_fields = ['first_name', 'last_name', 'email', 'phone', 'city']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    inlines = [DeveloperInline]

