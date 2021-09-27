from django.contrib import admin
from .models import Registeredusers
from .models import Adminusers

# Register your models here.
admin.site.register(Registeredusers)
admin.site.register(Adminusers)