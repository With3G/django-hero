from django.db import models
from apps.heroes.models import Hero
from django.utils.translation import ugettext_lazy as _


class Author(models.Model):

    created = models.DateTimeField(verbose_name=_('Created'), null=True, blank=True, auto_now_add=True)
    modified = models.DateTimeField(verbose_name=_('Updated'), null=True, blank=True, auto_now=True)

    name = models.CharField(verbose_name=_('Name'), max_length=255, null=True, blank=True)
    born = models.DateField(verbose_name=_('Born'), null=True, blank=True)
    heroes = models.ManyToManyField(Hero, verbose_name=_('Heroes'), blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')
