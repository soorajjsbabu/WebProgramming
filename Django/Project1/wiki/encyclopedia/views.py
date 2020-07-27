from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def article(request, title):
    print("Article triggered")
    md_file = util.get_entry(title)
    if not md_file:
        return render(request, "encyclopedia/404.html")
    return render(request, "encyclopedia/article.html", {
        "the_text": md_file
    })
