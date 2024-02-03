from django.contrib import admin

from .models import StudentModel, SchoolclassModel
# Register your models here.

class SchoolClassAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = ['name', 'slug']
    
    
admin.site.register(SchoolclassModel, SchoolClassAdmin)
admin.site.register(StudentModel)