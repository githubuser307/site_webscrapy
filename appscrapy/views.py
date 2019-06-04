from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
#from django.contrib.auth.views import LoginView, LogoutView
from .models import Jobs, Site, Category
from django.views.generic import View
from .utils import ObjectDetailMixin
from .forms import *
# Create your views here.
def jobs_list(request):
    jobs = Jobs.objects.all()
    return render(request, 'appscrapy/index.html', context = {'jobs': jobs})

def sites_list(request):
    sites = Site.objects.all()
    return render(request, 'appscrapy/sites_list.html', context={'sites': sites})

def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'appscrapy/categories_list.html', context={'categories': categories})


class JobDetail(ObjectDetailMixin, View):
    model = Jobs
    template = 'appscrapy/job_detail.html'


class SiteDetail(ObjectDetailMixin, View):
    model = Site
    template = 'appscrapy/site_detail.html'


class CategoryDetail(ObjectDetailMixin, View):
    model = Category
    template = 'appscrapy/category_detail.html'

class SiteCreate(View):

    def get(self, request):
        form = SiteForm()
        return render(request, 'appscrapy/site_create.html', context={'form': form})


#class JobCreate(JobForm):
