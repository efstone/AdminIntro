from django.db import models
from django.utils.safestring import mark_safe


class Company(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Companies'

# Disqus
# Instagram
# Knight Foundation
# MacArthur Foundation
# Mozilla
# National Geographic
# Open Knowledge Foundation
# Pinterest
# Open Stack


class Developer(models.Model):
    first_name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField(max_length=100, blank=True, default='')
    phone = models.CharField(max_length=50, blank=True, default='')
    street_address = models.CharField(max_length=100, blank=True, default='')
    city = models.CharField(max_length=100, blank=True, default='')
    state = models.CharField(max_length=50, blank=True, default='')
    zip_code = models.CharField(max_length=20, blank=True, default='')
    company = models.ForeignKey(Company, db_constraint=False, null=True, default=None, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def search_with_google(self):
        return mark_safe(f"<a href=\"https://www.google.com/search?q={self.street_address.replace(' ', '+')}+{self.city}+{self.state}\" target=\"_blank\">Map it</a>")

    class Meta:
        ordering = ['last_name', 'first_name']
