from django.conf.urls import url
from . import views

app_name = "career"


urlpatterns = [
    url(r'^$', views.jobs, name='jobs'),
    url(r'^(?P<job_id>[0-9]+)/$', views.jobDetails, name='jobDetails'),
    url(r'^career/$', views.career, name='career'),
    ]
