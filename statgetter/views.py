from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the statgetter index.")

def stats(request, repo_url):
    context = {
        'repo_url': repo_url,
        'contributors': {
            'headers': ['developer', 'commits', 'insertions', 'deletions'],
            'rows': [
                ['mark@mark.com', 1000, 10000, 20000],
                ['timmy@timmy.com', 10, 100, 0],
                ['john@john.com', 100, 1, 1000],
            ]
        }
    }
    return render(request, 'statgetter/stats.html', context)
