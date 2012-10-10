from django.contrib import admin
from services.models import Service
from sorl.thumbnail.admin import AdminImageMixin
from sorl.thumbnail import get_thumbnail

    
class ServiceAdmin(AdminImageMixin, admin.ModelAdmin):
    """docstring for FeaturedSlide"""

    def thumbnail(self, obj):
           im = get_thumbnail(obj.image, '60x60', quality=99)
           return u"<img src='%s'>" % im.url
    thumbnail.allow_tags = True
       
    list_display = ('title', 'position', 'status', 'thumbnail',)
    pass
        

admin.site.register(Service, ServiceAdmin)
