from django.db import models
from django.utils.translation import ugettext_lazy as _


class Hero(models.Model):

    name = models.CharField(verbose_name=_('Name'), max_length=255, null=True, blank=True)
    # TODO:
    # publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Hero')
        verbose_name_plural = _('Heroes')
