from xml.dom.minicompat import NodeList

from django.contrib import admin

from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','role', 'phone_number')
    search_fields = ('username', 'email')
    list_filter = ('role',)