from django import template
from news.models import Entry

register = template.Library()

@register.inclusion_tag('news/latest-entries.html', takes_context=True)
def latest_entries(context,limit=3):
    entries = Entry.objects.all()[:limit]
    return {'entries': entries, 'request': context['request']}
