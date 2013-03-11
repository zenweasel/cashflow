from datetime import datetime
from django.db import models
from django.contrib import admin

entry_type_choices = ((1, "Credit"), (2, "Debit"))


class RecurranceType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    unit_of_measure = models.CharField(max_length=20)
    quantity = models.IntegerField(null=True, blank=True)
    day_of_month = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.name

admin.site.register(RecurranceType)


class EntryCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    debit_credit = models.IntegerField(choices=entry_type_choices)

    class Meta:
        verbose_name_plural = "Entry Categories"

    def __repr__(self):
        return self.name

    def __unicode__(self):
        return self.name

admin.site.register(EntryCategory)


class Entry(models.Model):
    category = models.ForeignKey(EntryCategory)
    created_date = models.DateTimeField(auto_now_add=True)
    incurred_date = models.DateTimeField(default=datetime.now())
    name = models.CharField(max_length=100)
    reference_number = models.CharField(max_length=40)
    debit_credit = models.IntegerField(choices=entry_type_choices)
    description = models.TextField(null=True, blank=True)
    amount = models.DecimalField(decimal_places=2, max_digits=5)
    recurring = models.BooleanField(default=False)
    recurrance_type = models.ForeignKey(RecurranceType, null=True, blank=True)

    class Meta:
        unique_together = ['incurred_date', 'name']

    def __unicode__(self):
        return self.name

admin.site.register(Entry)



