from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from . import util
import random


def index(request):
    print("Index triggered")
    print(request)
    title = request.GET.get('q', None)
    if title:
        md_file = util.get_entry(title)
        if not md_file:
            return render(request, "encyclopedia/404.html")
        return render(request, "encyclopedia/article.html", {
            "the_text": md_file
        })
    else:
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

def random_page(request):
    print("Random triggered")
    entries = util.list_entries() 
    selected_page = random.choice(entries)
    return redirect('article', title=selected_page)

def new(request):
    return render(request, "encyclopedia/new.html")
    