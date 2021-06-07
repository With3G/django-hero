from django.db import models
from django.utils.translation import ugettext_lazy as _


class Publisher(models.Model):

    created = models.DateTimeField(verbose_name=_('Fecha de creación'), null=True, blank=True, auto_now_add=True)
    modified = models.DateTimeField(verbose_name=_('Fecha de modificación'), null=True, blank=True, auto_now=True)

    name = models.CharField(verbose_name=_('Name'), max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Publisher')
        verbose_name_plural = _('Publishers')
