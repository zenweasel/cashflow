from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.views.generic import View
from cashflow.forms import ExpenseForm
from models import Expense, Income
import logging


class ExpenseListView(View):
    """ List of Expenses
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
        expenses = Expense.objects.all()
        return expenses


class ExpenseCreateView(View):
    """Displays the details of an Expense"""

    def get(self, request, *args, **kwargs):
        self.kwargs = kwargs
        return TemplateResponse(request, self.get_template_name(),
                                self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = ExpenseForm(request.POST)
        if form.is_valid():
            ex = Expense()
            ex.amount = form.cleaned_data['amount']
            ex.name = form.cleaned_data['name']
            ex.description = form.cleaned_data['description']
            ex.incurred_date = form.cleaned_data['incurred_date']
            ex.category = form.cleaned_data['category']
            ex.save()

            return TemplateResponse(request, self.get_template_name(), {"form": form})
        else:
            return TemplateResponse(request, self.get_template_name(),
                                self.get_context_data())

    def get_template_name(self):
        """Returns the name of the template we should render"""
        return "expense_create.html"

    def get_context_data(self):
        """Returns the data passed to the template"""
        return {
            "form": ExpenseForm(),
            }


class ExpenseDetailView(View):
    """Displays the details of an Expense"""

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
        return get_object_or_404(Expense, pk=self.kwargs.get("pk"))


class ExpenseImportView(View):
    """Import Expenses from Bank Statements"""

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
        return get_object_or_404(Expense, pk=self.kwargs.get("pk"))