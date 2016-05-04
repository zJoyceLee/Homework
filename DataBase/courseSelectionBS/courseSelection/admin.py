from django.contrib import admin

# Register your models here.
from courseSelection.models import S
from courseSelection.models import C
from courseSelection.models import SC

admin.site.register(S)
admin.site.register(C)
admin.site.register(SC)
