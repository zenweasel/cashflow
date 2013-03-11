from django import forms
from models import EntryCategory, RecurranceType
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

entry_type_choices = ((1, "Credit"), (2, "Debit"))


class EntryForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-EntryForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = '/cashflow/entry/create'

        self.helper.add_input(Submit('submit', 'Submit'))
        super(EntryForm, self).__init__(*args, **kwargs)

    debit_credit = forms.ChoiceField(choices=entry_type_choices)
    incurred_date = forms.DateTimeField()
    name = forms.CharField(max_length=100)
    reference_number = forms.CharField(required=False)
    description = forms.CharField(required=False)
    amount = forms.DecimalField()
    category = forms.ModelChoiceField(queryset=EntryCategory.objects.all())
    recurring = forms.BooleanField()
    recurring_type = forms.ModelChoiceField(queryset=RecurranceType.objects.all())
