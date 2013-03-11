from django.conf.urls import patterns, url
from views import EntryDetailView, EntryImportView, EntryListView, EntryCreateView


urlpatterns = patterns('',

                       url(r'entry/list', EntryListView.as_view()),
                       url(r'entry/detail/$', EntryDetailView.as_view()),
                       url(r'entry/import$', EntryImportView.as_view()),
                       url(r'entry/create$', EntryCreateView.as_view()),
)