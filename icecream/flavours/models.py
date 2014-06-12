from django.db import models

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
    title = models.CharField(max_length=200)
    scoops = models.IntegerField()

    def __unicode__(self):
        return self.title