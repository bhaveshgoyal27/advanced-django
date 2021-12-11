from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class CustomUserAdmin(UserAdmin):
	model = CustomUser
	add_form = CustomUserCreationForm

	fieldsets = (
		(None, {'fields': ('email', 'password', )}),
		(('Personal info'), {'fields': ('first_name', 'last_name')}),
		(('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
			'groups', 'user_permissions')}),
		(('Important dates'), {'fields': ('last_login', 'date_joined')}),
		(('user_info'), {'fields': ('is_director', 'is_producer')}),
  )

admin.site.register(CustomUser,CustomUserAdmin)