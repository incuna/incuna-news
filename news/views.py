from django.shortcuts import render_to_response
from django.template.context import RequestContext
from models import Entry

def category_object_list(request, category, extra_context = None):

    context = RequestContext(request)

    if extra_context != None:
        context.update(extra_context)

    latest = Entry.objects.filter(category__slug=category)

    context.update({'latest':latest,})

    return render_to_response('news/entry_archive.html', context)