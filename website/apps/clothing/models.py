from django.db import models
from django.db.models.fields.files import ImageField
from django_extensions.db.fields import *
from django.utils.translation import ugettext as _



""" BASE MODEL """
class BaseModel(models.Model):
    uuid = UUIDField()
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        abstract = True


class ClothingTime(BaseModel):
    name = models.CharField(_('Name'), max_length=256, blank=True)
    slug = AutoSlugField(populate_from='name')
    image = ImageField(_('Image'), upload_to="clothing_app/times/", null=True, blank=True)

    def __unicode__(self):
        return u"%s" % self.name

    """ Meta """
    class Meta:
        app_label = 'clothing'
        verbose_name = _('Clothing time')
        verbose_name_plural = _('Clothing times')
        ordering = ('-created', )