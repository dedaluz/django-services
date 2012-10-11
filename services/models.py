from django.db import models
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField
from django.db.models import permalink

from managers import PublicManager


from django.db import models
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField
from flexslider.models import Slider
from django.db.models import permalink

from managers import PublicManager

class ServiceGroup(models.Model):
    name = models.CharField(_("name"), max_length=50, unique=True)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = u'ServiceGroup'
        verbose_name_plural = u'ServiceGroups'
    
    def __unicode__(self):
        return self.name
        
class Service(models.Model):
    """
    (Featured description)
    """
    STATUS_CHOICES = (
        (0, _('Private')),
        (1, _('Draft')),
        (2, _('Public')),
        (3, _('Featured')),
    )
    service_group = models.ForeignKey( ServiceGroup, related_name="services")
    slider = models.ForeignKey(Slider, blank=True)
    title = models.CharField(_('title'), max_length=150)
    slug = models.SlugField(unique=True)
    caption = models.TextField(_('caption'), blank=True)
    excerpt = models.TextField(_('excerpt'), blank=True)
    description = models.TextField(_('description'))
    price_notes = models.TextField(_('price notes'), blank=True)
    
    icon  = ImageField(_('icon'), upload_to='services/icons', blank=True)
    banner  = ImageField(_('banner'), upload_to='services/banners', blank=True)
    status  = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=2)
    
    # position field
    position = models.PositiveSmallIntegerField("Position", default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = PublicManager()
    
    class Meta:
        verbose_name = u'Service'
        verbose_name_plural = u'Services'
        ordering = ('position',)
    
    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('service_detail', None, { 'slug':self.slug })
