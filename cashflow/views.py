from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.views.generic import View
from cashflow.forms import EntryForm
from models import Entry


class EntryListView(View):
    """ List of Entrys
    """

    def get(self, request, *args, **kwargs):
        self.kwargs = kwargs
        return TemplateResponse(request, self.get_template_name(),
                                self.get_context_data())

    def get_template_name(self):
        """Returns the name of the template we should render"""
        return "expense_list.html"

    def get_context_data(self):
        """Returns the data passed to the template"""
        return {
            "expenses": self.get_object(),
            }

    def get_object(self):
        """Returns the BlogPost instance that the view displays"""
        expenses = Entry.objects.all()
        return expenses


class EntryCreateView(View):
    """Displays the details of an Entry"""

    def get(self, request, *args, **kwargs):
        self.kwargs = kwargs
        return TemplateResponse(request, self.get_template_name(),
                                self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = EntryForm(request.POST)
        if form.is_valid():
            ex = Entry()
            ex.amount = form.cleaned_data['amount']
            ex.name = form.cleaned_data['name']
            ex.description = form.cleaned_data['description']
            ex.incurred_date = form.cleaned_data['incurred_date']
            ex.category = form.cleaned_data['category']
            ex.recurring = False
            ex.recurrance_type = form.cleaned_data['recurring_type']
            ex.debit_credit = form.cleaned_data['debit_credit']
            ex.reference_number = form.cleaned_data['reference_number']
            ex.save()

            return TemplateResponse(request, self.get_template_name(), {"form": EntryForm(), 'success': True})
        else:
            return TemplateResponse(request, self.get_template_name(),
                                self.get_context_data(form=form))

    def get_template_name(self):
        """Returns the name of the template we should render"""
        return "expense_create.html"

    def get_context_data(self, form=None):
        """Returns the data passed to the template"""
        if form is not None:
            return {
                "form": form,
                }
        else:

            return {
                "form": EntryForm(),
                }


class EntryDetailView(View):
    """Displays the details of an Entry"""

    def get(self, request, *args, **kwargs):
        self.kwargs = kwargs
        return TemplateResponse(request, self.get_template_name(),
                                self.get_context_data())

    def get_template_name(self):
        """Returns the name of the template we should render"""
        return "expense_detail.html"

    def get_context_data(self):
        """Returns the data passed to the template"""
        return {
            "expense": self.get_object(),
            }

    def get_object(self):
        """Returns the BlogPost instance that the view displays"""
        return get_object_or_404(Entry, pk=self.kwargs.get("pk"))


class EntryImportView(View):
    """Import Entrys from Bank Statements"""

    def get(self, request, *args, **kwargs):
        self.kwargs = kwargs
        return TemplateResponse(request, self.get_template_name(),
                                self.get_context_data())

    def get_template_name(self):
        """Returns the name of the template we should render"""
        return "blog/blogpost_detail.html"

    def get_context_data(self):
        """Returns the data passed to the template"""
        return {
            "blogpost": self.get_object(),
            }

    def get_object(self):
        """Returns the BlogPost instance that the view displays"""
        return get_object_or_404(Entry, pk=self.kwargs.get("pk"))