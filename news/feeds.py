from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from models import Entry
import datetime

from django.contrib.sites.models import Site

class WeblogEntryFeed(Feed):

    def title(self):
        return "%s latest News" % Site.objects.get_current().name

    def link(self):
        return reverse('news_archive_index')

    def description(self):
        return "Latest news about %s" % Site.objects.get_current().name

    def items(self):
        return Entry.objects.filter(pub_date__lte=datetime.datetime.now())[:10]

    def item_title(self, item):
        return item.headline

    def item_description(self, item):
        return item.headline
    
