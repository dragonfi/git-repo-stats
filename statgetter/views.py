from collections import OrderedDict

from django.shortcuts import render
from django.http import HttpResponse

from .gitstats import RemoteRepoStats


def index(request):
    return HttpResponse("Hello, world. You're at the statgetter index.")

def stats(request, repo_url):
    contributions = RemoteRepoStats(repo_url).contributions_by_author
    context = {
        'repo_url': repo_url,
        'contributions_header': ['name', 'commits', 'insertions', 'deletions'],
        'contributions': OrderedDict(sorted(contributions.items())),
    }
    return render(request, 'statgetter/stats.html', context)
