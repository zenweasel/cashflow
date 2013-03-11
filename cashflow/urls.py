from django.conf.urls import patterns, url
from views import ExpenseDetailView, ExpenseImportView, ExpenseListView, ExpenseCreateView


urlpatterns = patterns('',

                       url(r'expense/list', ExpenseListView.as_view()),
                       url(r'expense/detail/$', ExpenseDetailView.as_view()),
                       url(r'expense/import$', ExpenseImportView.as_view()),
                       url(r'expense/create$', ExpenseCreateView.as_view()),
)