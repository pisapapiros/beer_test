from django.db import models
from django.utils.translation import ugettext_lazy as _


class Bar(models.Model):
    name = models.CharField(_('Name'), max_length=255)

    class Meta:
        verbose_name = _("Bar")
        verbose_name_plural = _("Bar")
        ordering = ['-name']

    def __str__(self):
        return self.name
