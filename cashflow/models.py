from datetime import datetime
from django.db import models
from django.contrib import admin


class RecurranceType(models.Model):
    time_units_of_measure = (
        (1, 'Day'),
        (2, 'Week'),
        (3, 'Month'),
        (4, 'Year'),
    )
    name = models.CharField(max_length=100, unique=True)
    unit_of_measure = models.IntegerField(choices=time_units_of_measure)
    quantity = models.IntegerField(null=True, blank=True)
    day_of_month = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.name

admin.site.register(RecurranceType)


class EntryCategory(models.Model):
    entry_type_choices = ((1, "Credit"), (2, "Debit"))
    name = models.CharField(max_length=100, unique=True)
    debit_credit = models.IntegerField(choices=entry_type_choices)

    class Meta:
        verbose_name_plural = "Entry Categories"

    def __repr__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.name

admin.site.register(EntryCategory)


class Entry(models.Model):
    category = models.ForeignKey(EntryCategory)
    created_date = models.DateTimeField(auto_now_add=True)
    incurred_date = models.DateTimeField(auto_now_add=True, verbose_name='Date Spent', db_index=True)
    name = models.CharField(max_length=100)
    reference_number = models.CharField(max_length=40, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    amount = models.DecimalField(decimal_places=2, max_digits=5)
    recurring = models.BooleanField(default=False)
    recurrance_type = models.ForeignKey(RecurranceType, null=True, blank=True)

    class Meta:
        unique_together = ['incurred_date', 'name']
        verbose_name_plural = 'Entries'

    def __unicode__(self):
        return u'%s' % self.name

    def as_dict(self):
        entry = dict()
        entry['entry_id'] = self.id
        entry['category'] = self.category
        entry['incurred_date'] = self.incurred_date
        entry['name'] = self.name
        entry['reference_number'] = self.reference_number
        entry['amount'] = self.amount
        entry['recurring'] = self.recurring
        entry['recurrance_type'] = self.recurrance_type
        return entry

admin.site.register(Entry)
