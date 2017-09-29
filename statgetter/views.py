from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the statgetter index.")

def stats(request, repo_url):
    context = {
        'repo_url': repo_url,
    }
    return render(request, 'statgetter/stats.html', context)
