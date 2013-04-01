from django.conf.urls import patterns, url
from views import EntryEditView, EntryImportView, EntryListView, EntryCreateView, EntryDeleteView

urlpatterns = patterns('',
                       url(r'entry/list', EntryListView.as_view(), {'title': 'List Entries'}, name='entry-list'),
                       url(r'entry/edit/(?P<entry_id>\d*)$', EntryEditView.as_view(),
                           {'action': 'edit','title': 'Edit Entry'}),
                       url(r'entry/import$', EntryImportView.as_view()),
                       url(r'entry/create$', EntryCreateView.as_view(),
                           {'action': 'add', 'title': 'Create Entry'}),
                       url(r'entry/delete/(?P<entry_id>\d*)$', EntryDeleteView.as_view(),
                           {'action': 'delete','title': 'Delete Entry'}),
)