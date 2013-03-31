from django import forms
from django.forms import DateTimeInput
from models import EntryCategory, RecurranceType
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, HTML
from datetime import datetime

entry_type_choices = ((1, "Credit"), (2, "Debit"))


class EntryForm(forms.Form):
    """
    Main Entry form for edit/create
    """
    entry_id = forms.HiddenInput()
    debit_credit = forms.ChoiceField(choices=entry_type_choices)
    incurred_date = forms.DateTimeField(initial=datetime.now(), widget=DateTimeInput)
    name = forms.CharField(max_length=100)
    reference_number = forms.CharField(required=False)
    description = forms.CharField(required=False)
    amount = forms.DecimalField()
    category = forms.ModelChoiceField(queryset=EntryCategory.objects.all())
    recurring = forms.BooleanField(initial=False, required=False)
    recurring_type = forms.ModelChoiceField(queryset=RecurranceType.objects.all(), required=False)
    entry_form_layout = Layout(
        Div('incurred_date', css_class="span2"),
        Div('name', css_class="span2 offset1"),
        Div('amount', css_class="span1 offset1"),
        HTML('<div class="row"></div>'),
        Div('category', css_class="span2", ),
        Div('reference_number', css_class='span2 offset1'),
        Div('description', css_class='span2 offset1'),
        HTML('<div class="row"></div>'),
        Div('debit_credit', css_class='span2 extended'),
        Div('recurring', css_class='span2 offset1 extended'),
        Div('recurring_type', css_class='span2 offset1 extended'),
        HTML('<div class="row"></div>'),
    )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-EntryForm'
        self.helper.form_class = 'blueForms'
        self.helper.add_input(Submit('submit', 'Submit'))

        if kwargs.get('action', None) is 'add':
            self.helper.form_method = 'post'
            self.helper.form_action = '/cashflow/entry/create/'
        if kwargs.get('action', None) is 'edit':
            self.helper.form_action = '/cashflow/entry/edit/'
            self.helper.form_method = 'post'
        ex = kwargs.get('entry', None)
        if ex is not None:
            self.entry_id = ex.id
            self.amount = ex.amount
            self.category = ex.category
            self.name = ex.name
            self.debit_credit = ex.debit_credit
            self.incurred_date = ex.incurred_date
            self.reference_number = ex.reference_number
            self.description = ex.description
            self.recurring = ex.recurring
            self.recurrance_type = ex.recurrance_type

        self.helper.layout = self.entry_form_layout
        super(EntryForm, self).__init__(*args, **kwargs)

    def bind(self, ex):
        self.entry_id = ex.id
        self.amount = ex.amount
        self.category = ex.category
        self.name = ex.name
        self.debit_credit = ex.debit_credit
        self.incurred_date = ex.incurred_date
        self.reference_number = ex.reference_number
        self.description = ex.description
        self.recurring = ex.recurring
        self.recurrance_type = ex.recurrance_type

