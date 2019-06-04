from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Jobs(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(blank=True, max_length=150, db_index=True)
    date_create = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=150, unique=True)
    throtling = models.IntegerField(default=0)
    numThread = models.IntegerField(default=1)
    proxy = models.BooleanField(default=False)
    state = models.CharField(max_length=150, db_index=True, default='new')
    site = models.ManyToManyField('Site', blank=False, related_name='jobs')
    category = models.ManyToManyField('Category', blank=False, related_name='jobs')
    date_start = models.DateTimeField(null=True, blank=True)
    date_end = models.DateTimeField(null=True, blank=True)
    comment = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('job_detail_url', kwargs={'id': self.id})

    def __str__(self):
        return self.slug


class Site(models.Model):
    id = models.AutoField(primary_key=True)
    date_create = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, db_index=True, unique=True)
    start_url = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('site_detail_url', kwargs={'id': self.id})


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    date_create = models.DateTimeField(auto_now_add=True)
    site = models.ManyToManyField('Site', blank=False, related_name='categories')
    name = models.CharField(max_length=150, db_index=True, unique=True)
    start_url = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail_url', kwargs={'id': self.id})
