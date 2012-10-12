from django.conf import settings
from django.conf.urls.defaults import *
from .models import Entry
from .feeds import WeblogEntryFeed

info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'pub_date',
}

tagging_dict = {
    'queryset_or_model': Entry,
}

if hasattr(settings, 'NEWS_NUM_LATEST'):
    info_dict_index = {'num_latest': settings.NEWS_NUM_LATEST}
    info_dict_index.update(info_dict)
else:
    info_dict_index = info_dict


urlpatterns = patterns('',
        url(r'^feed/$', WeblogEntryFeed(), name='news_feed'),
        # the date based generic view requires a day name, which is unnecessay unless you're posting more than one post a day., so we're using object detail instead.
        url(r'^(\d{4})/(\d{2})/(?P<slug>[\w-]+)/$', 'django.views.generic.list_detail.object_detail', dict(queryset=Entry.objects.all(), slug_field='slug'), name='news_detail'),
        #url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$', 'archive_day', info_dict, name='news_archive_day'),
        url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', 'django.views.generic.date_based.archive_month', dict(info_dict, month_format='%m'), name='news_archive_month'),
        url(r'^(?P<year>\d{4})/$', 'django.views.generic.date_based.archive_year', info_dict, name='news_archive_year'),
        url(r'^tags/(?P<tag>.*)/$', 'tagging.views.tagged_object_list', tagging_dict, name='news_archive_tagged',),
        url(r'^category/(?P<category>.*)/$', 'news.views.category_object_list', name='news_archive_category',),
        url(r'^/?$', 'django.views.generic.date_based.archive_index', info_dict_index, name='news_archive_index',),
        )
