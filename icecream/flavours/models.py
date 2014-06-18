from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    updating ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Flavour(TimeStampedModel):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    slug = models.SlugField()
    scoops_remaining = models.IntegerField(null=True, blank=True)

    def get_absolute_url(self):
          return reverse("flavours:detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)
        models.Model.save(self, *args, **kwargs)

    def __unicode__(self):
        return self.name