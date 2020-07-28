from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from . import util
from django.contrib import messages

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
        "the_text": md_file,
        "title": title 
    })

def random_page(request):
    print("Random triggered")
    entries = util.list_entries() 
    selected_page = random.choice(entries)
    return redirect('article', title=selected_page)

def new(request):
    return render(request, "encyclopedia/new.html")

def add_article(request):
    print("Add article triggered")
    title = request.POST['title']
    content = request.POST['content']
    print(title, content)
    try:
        util.save_entry(title, content)   
    except FileExistsError:
        messages.add_message(request, messages.ERROR, 'Title already exists')
    return redirect('new')
    
def edit(request, title):
    if request.method == "GET":
        md_file = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title, 
            "content": md_file
        })
    if request.method == "POST":
        print("Post method")
        print(request.POST)
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content, update = True)   
        return redirect('article', title=title)
