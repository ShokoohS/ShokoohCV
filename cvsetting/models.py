from django.db import models


# Create your models here.

class SiteSetting(models.Model):
    title = models.CharField(max_length=150)
    mobile = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    about_us = models.TextField(null=True, blank=True)
    github_link = models.CharField(null=True, blank=True, max_length=200)
    persian_cv_link = models.CharField(null=True, blank=True, max_length=200)
    english_cv_link = models.CharField(null=True, blank=True, max_length=200)

    class Meta:
        verbose_name = 'mySetting'
        verbose_name_plural = 'mySetting'

    def __str__(self):
        return self.title
