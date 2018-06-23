from django.db import models


class job(models.Model):
    job_title = models.CharField(max_length=250)
    job_profile = models.CharField(max_length=250)
    job_description = models.TextField(default=None, blank=True)
    requirements = models.TextField(default=None, blank=True)
    salary = models.CharField(max_length=250, default=None, blank=True, null=True)
    experience = models.CharField(max_length=250, default=None, blank=True, null=True)

    def __str__(self):
        return self.job_title

