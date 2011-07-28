import datetime
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from incuna.db.models import *
from tagging.fields import TagField

from feincms.models import Base
from feincms.content.medialibrary.models import MediaFileContent
from feincms.content.richtext.models import RichTextContent


class NewsCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, help_text='This will be automatically generated from the name', unique=True,)

    class Meta:
        verbose_name_plural = 'news categories'

    def __unicode__(self):
        return self.name
    
class Entry(Base):
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    headline = models.CharField(max_length=255)
    slug = AutoSlugField(max_length=255,populate_from="headline",help_text='This will be automatically generated from the name',unique=True,editable=True)
    category = models.ForeignKey(NewsCategory, null=True, blank=True)
    tags = TagField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'entries'
        ordering = ('-pub_date',)
        get_latest_by = 'pub_date'

    def __unicode__(self):
        return self.headline

    def get_absolute_url(self):
        return ('news_detail', (self.pub_date.strftime("%Y"), self.pub_date.strftime("%m"), self.slug))
    get_absolute_url = models.permalink(get_absolute_url)

Entry.register_regions(
    ('summary', 'Summary'),
    ('main', 'Main article'),
    )

Entry.create_content_type(RichTextContent)
Entry.create_content_type(MediaFileContent, POSITION_CHOICES=(('default', _('Default')),))
