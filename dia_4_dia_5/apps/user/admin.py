from django.contrib import admin
from apps.user.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    
    model = User
    fields = ['name', 'email']