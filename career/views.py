from django.shortcuts import render, get_object_or_404
from .models import job


def jobs(request):
    alljobs = job.objects.all()
    return render(request, 'career/jobs.html', {'alljobs': alljobs})


def jobDetails(request, job_id):
    jobx = get_object_or_404(job, pk=job_id)
    return render(request, 'career/jobdetails.html', {'jobx': jobx})


def career(request):
  return render(request, 'career/career.html')


