from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin 
from django.contrib.admin.models import LogEntry, CHANGE
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import force_str
from django.core.exceptions import ValidationError
# from administration.admission.models import CustomUser
from .models import *
from .forms import *


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active', )
    list_filter = ('email', 'is_staff', 'is_active', )
    fieldsets = (
        (None, {'fields': ('first_name', 'middle_name', 'last_name','email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'middle_name', 'last_name', 'email', 'password1', 'password2', 'is_staff', 'is_active',)}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

class ApplicationAdmin(admin.ModelAdmin):
    model= Application
    fields =['name', 'Application_status' ]
    # list_display = __all__
    list_display = ('surname', 'course', 'email', 'phone_no', 'address', 'date_joined', 'Application_Status', 'message')
    actions= ['approve_application', 'reject_application']

    def approve_application(self, request, queryset):
        queryset.update(Application_Status='Approved')
        self.message_user(request, "Application Approved")
        for obj in queryset:
            LogEntry.objects.log_action(
                user_id=request.user.id,
                content_type_id=ContentType.objects.get_for_model(obj).pk,
                object_id=obj.id,
                object_repr=force_str(obj),
                action_flag=CHANGE,
                change_message="Application Approved",
            )
    
    def reject_application(self, request, queryset):
        queryset.update(Application_Status='Rejected')
        self.message_user(request, "Application Rejected")
        for obj in queryset:
            LogEntry.objects.log_action(
                user_id=request.user.id,
                content_type_id=ContentType.objects.get_for_model(obj).pk,
                object_id=obj.id,
                object_repr=force_str(obj),
                action_flag=CHANGE,
                change_message="Application Rejected",
            )


# Register your models here.
admin.site.register(Students)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Profile)
