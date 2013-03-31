from django.conf.urls import patterns, url
from views import EntryEditView, EntryImportView, EntryListView, EntryCreateView

urlpatterns = patterns('',
                       url(r'entry/list', EntryListView.as_view()),
                       url(r'entry/edit/(?P<entry_id>\d*)$', EntryEditView.as_view(),
                           {'action': 'edit','title': 'Edit Entry'}),
                       url(r'entry/import$', EntryImportView.as_view()),
                       url(r'entry/create$', EntryCreateView.as_view(),
                           {'action': 'add', 'title': 'Create Entry'}),
)