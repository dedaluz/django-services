from django.contrib import admin
from services.models import Package, Service, ServiceGroup
from sorl.thumbnail.admin import AdminImageMixin
from sorl.thumbnail import get_thumbnail

class ServiceInlineAdmin(AdminImageMixin, admin.TabularInline):
    model = Service
    fields = ('title', 'position', 'icon', 'status', )
    # define the sortable
    sortable_field_name = "position"
    extra = 0

class ServiceGroupAdmin(admin.ModelAdmin):
    list_display = ('name', )
    prepopulated_fields = {"slug": ("name",)} 
    
    inlines = [ServiceInlineAdmin]
    
class PackageInlineAdmin(AdminImageMixin, admin.TabularInline):
    model = Package
    fields = ('title', 'price', 'price_time', 'features', 'status', )
    # define the sortable
    extra = 0

class PackageAdmin(AdminImageMixin, admin.ModelAdmin):
    """docstring for Package"""
    
    prepopulated_fields = {"slug": ("title",)}   
    list_display = ('title', 'price', 'price_time', 'status',)
    
class ServiceAdmin(AdminImageMixin, admin.ModelAdmin):
    """docstring for Service"""

    def thumbnail(self, obj):
           im = get_thumbnail(obj.icon, '60x60', format='PNG', quality=99)
           return u"<img src='%s'>" % im.url
    thumbnail.allow_tags = True
    
    prepopulated_fields = {"slug": ("title",)}   
    list_display = ('title', 'position', 'status',)
    
    inlines = [PackageInlineAdmin]
        

admin.site.register(ServiceGroup, ServiceGroupAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Package, PackageAdmin)
