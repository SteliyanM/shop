from django.db import models
from django.template.defaultfilters import slugify


class Timestamps(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SlugFieldMixin(models.Model):
    class Meta:
        abstract = True

    slug = models.SlugField(
        null=False,
        blank=False,
        unique=True,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)