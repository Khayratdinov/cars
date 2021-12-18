from django.contrib import admin
from cars.models import Car, Image
from django.utils.html import format_html





class CarImageInline(admin.TabularInline):
    model = Image 
    extra = 4
 
class CarAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" height="40" style="border-radius: 50px" />'.format(object.car_photo.url))
    
    thumbnail.short_description = 'Cars Image'
    list_display = ['thumbnail', 'title','color', 'model' , 'body_style' ,'price', 'is_featured',]
    list_display_links = ('thumbnail', 'title',)
    list_editable = ('is_featured',)
    search_fields = ('id', 'title', 'city', 'model', 'body_style','fuel_type')
    list_filter = ('city', 'model', 'body_style', 'fuel_type')
    inlines = [CarImageInline]
    prepopulated_fields = {'slug':('title',)}


admin.site.register(Car, CarAdmin)
admin.site.register(Image)
