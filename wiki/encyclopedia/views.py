from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.defaultfilters import safe
from markdown2 import markdown
from django import forms
from django.urls import reverse
import random

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = util.get_entry(title)
    if content == None:
        return render(request, "encyclopedia/error.html")

    html_content = markdown(content)
    #print(html_content)
    #html_content.convert(content)

    return render(request, "encyclopedia/entry.html", {
        "content": html_content,
        "title": title
    })

def query(request):
    if request.method == "POST":
        qsearch = request.POST["q"]
        search_results_list = []
        for one_entry in util.list_entries():
            if str.lower(qsearch) == str.lower(one_entry):
                return entry(request, qsearch)
            if str.lower(qsearch) in str.lower(one_entry):
                search_results_list.append(one_entry)

        return render(request, "encyclopedia/search_results.html", {
            "search_results": search_results_list
        })

def edit(request, title):
    content = util.get_entry(title)
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "content": content,
    })

def save(request, title):
    if request.method == "POST":
        content = str(request.POST["text_area"])
        util.save_entry(title, content)
        return HttpResponseRedirect(reverse("wiki:index"))
        #return HttpResponse(title + " : " + content)

def new_entry(request):
    return render(request, "encyclopedia/new_entry.html")
    #return HttpResponse("New Entry")

def save_new_entry(request):
    if request.method == "POST":
        title = str(request.POST["title"])
        content = str(request.POST["text_area"])
        util.save_entry(title, content)
        return HttpResponseRedirect(reverse("wiki:index"))
        #return HttpResponse(title + " : " + content)

def random_page(request):
    random_entry = random.choice(util.list_entries())
    content = util.get_entry(random_entry)
    html_content = markdown(content)
    #return HttpResponse(random_entry)

    return render(request, "encyclopedia/entry.html", {
        "title": random_entry,
        "content": html_content
    })