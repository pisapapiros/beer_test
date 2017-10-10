from django.db import models
from django.utils.translation import ugettext_lazy as _


def beer_image_upload_location(instance, filename):
    return 'media/beer/images/%s.png' % (instance.id)


class Beer(models.Model):
    COLOR_YELLOW = 1
    COLOR_AMBER = 2
    COLOR_BROWN = 3
    COLOR_BLACK = 4

    COLOR_CHOICES = (
        (COLOR_YELLOW, _(u'Yellow')),
        (COLOR_AMBER, _(u'Amber')),
        (COLOR_BROWN, _(u'Brown')),
        (COLOR_BLACK, _(u'Black'))
    )

    name = models.CharField(_('Name'), max_length=255)
    abv = models.DecimalField(_(u'Alcohol by volume'), max_digits=5, decimal_places=2, default=0)
    color = models.PositiveSmallIntegerField(_(u'Color'), choices=COLOR_CHOICES, default=COLOR_YELLOW)
    is_filtered = models.BooleanField(_("Is filtered?"), default=False)
    creation_date = models.DateTimeField(_(u"Creation date"), auto_now_add=True)
    image = models.ImageField(_(u"Image"), blank=True, null=True, upload_to=beer_image_upload_location, max_length=400)

    class Meta:
        verbose_name = _("Beer")
        verbose_name_plural = _("Beers")
        ordering = ['-name']

    def __str__(self):
        return self.name
