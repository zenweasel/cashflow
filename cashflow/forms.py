from django import forms
from models import ExpenseCategory, RecurranceType


class ExpenseForm(forms.Form):
    incurred_date = forms.DateTimeField()
    name = forms.CharField(max_length=100)
    description = forms.CharField()
    amount = forms.DecimalField()
    category = forms.ModelChoiceField(queryset=ExpenseCategory.objects.all())
    recurring = forms.BooleanField()
    recurring_type = forms.ModelChoiceField(queryset=RecurranceType.objects.all())
