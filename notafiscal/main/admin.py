from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class AdminCustomUser(UserAdmin):
    model = CustomUser
    list_display = ['id','email','registrationNumber','is_active']
    list_display_links = ('id','email','registrationNumber','is_active',)
    fieldsets = (
        (None, {'fields':('email','password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions',)}),
        ('Management', {'fields': ('last_login',)}),
        ('Custom fields', {'fields': ('registrationNumber', 'phoneNumber', 'is_email_verified','name',)}),
    )
    filter_horizontal = ('groups', 'user_permissions',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'groups', 'user_permissions',)
        }),
    )
    search_fields = ['email',]
    ordering = ['email']

admin.site.register(CustomUser,AdminCustomUser)

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ProductFiles)
admin.site.register(Invoice)
admin.site.register(InvoiceItem)
admin.site.register(Warranty)
