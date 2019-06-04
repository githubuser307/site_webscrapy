

from django.urls import path
from .views import *

urlpatterns = [
    path('', jobs_list, name='jobs_list_url'),
    #path('job/create/', JobCreate.as_view(), name='job_create_url'),
    path('job/<id>/', JobDetail.as_view(), name='job_detail_url'),
    path('sites/', sites_list, name='sites_list_url' ),
    path('site/create/', SiteCreate.as_view(), name='site_create_url'),
    path('site/<id>/', SiteDetail.as_view(), name='site_detail_url'),
    path('categories/', categories_list, name='categories_list_url'),
    path('category/<id>/', CategoryDetail.as_view(), name='category_detail_url'),
]

