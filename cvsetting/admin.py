from django.contrib import admin

# Register your models here.
from cvsetting.models import SiteSetting

admin.site.register(SiteSetting)