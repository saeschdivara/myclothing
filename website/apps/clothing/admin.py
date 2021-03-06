from django.contrib import admin

from clothing.models import ClothingTime, Clothing, BodyPart


"""  CLOTHING TIME ADMIN """
class ClothingTimeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'modified', )
    list_filter = ('name', 'created', 'modified',  )

admin.site.register(ClothingTime, ClothingTimeAdmin)


"""  CLOTHING ADMIN """
class ClothingAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'modified', )
    list_filter = ('name', 'created', 'modified',  )

admin.site.register(Clothing, ClothingAdmin)


"""  CLOTHING ADMIN """
class BodyPartAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'modified', )
    list_filter = ('name', 'created', 'modified',  )

admin.site.register(BodyPart, BodyPartAdmin)