from django.contrib import admin

from clothing.models import ClothingTime



"""  MAILING SOURCE ADMIN """
class ClothingTimeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'modified', )
    list_filter = ('name', 'created', 'modified',  )

admin.site.register(ClothingTime, ClothingTimeAdmin)