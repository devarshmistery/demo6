from django.contrib import admin

# Register your models here.
from .models import HomePage,Admin_reg, Notice_view, Profile_view, Complaint_view
admin.site.register(HomePage)
admin.site.register(Admin_reg)
admin.site.register(Notice_view)
admin.site.register(Profile_view)
admin.site.register(Complaint_view)