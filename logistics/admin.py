from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

@admin.register(MIS)
class userdat(ImportExportModelAdmin):
    pass


@admin.register(VC_NO)
class userdat(ImportExportModelAdmin):
    pass

admin.site.register(MisFull)