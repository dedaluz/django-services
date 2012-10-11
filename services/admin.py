from django.contrib import admin
from services.models import Service, ServiceGroup
from sorl.thumbnail.admin import AdminImageMixin
from sorl.thumbnail import get_thumbnail

class ServiceInlineAdmin(AdminImageMixin, admin.TabularInline):
    model = Service
    fields = ('title', 'position', 'image', 'status', )
    # define the sortable
    sortable_field_name = "position"
    extra = 0

class ServiceGroupAdmin(admin.ModelAdmin):
    list_display = ('name', )
    prepopulated_fields = {"slug": ("name",)} 
    
    inlines = [ServiceInlineAdmin]

class ServiceAdmin(AdminImageMixin, admin.ModelAdmin):
    """docstring for FeaturedSlide"""

    def thumbnail(self, obj):
           im = get_thumbnail(obj.image, '60x60', format='PNG', quality=99)
           return u"<img src='%s'>" % im.url
    thumbnail.allow_tags = True
    
    prepopulated_fields = {"slug": ("title",)}   
    list_display = ('title', 'position', 'status', 'thumbnail',)
    pass
        

admin.site.register(ServiceGroup, ServiceGroupAdmin)
admin.site.register(Service, ServiceAdmin)
