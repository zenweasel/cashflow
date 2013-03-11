from datetime import datetime
from django.db import models
from django.contrib import admin


class RecurranceType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    unit_of_measure = models.CharField(max_length=20)
    quantity = models.IntegerField()

    def __unicode__(self):
        return self.name

admin.site.register(RecurranceType)


class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Expense Categories"

    def __repr__(self):
        return self.name

    def __unicode__(self):
        return self.name


admin.site.register(ExpenseCategory)


class IncomeCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Income Categories"

    def __repr__(self):
        return self.name

    def __unicode__(self):
        return self.name

admin.site.register(IncomeCategory)


class Entry(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    incurred_date = models.DateTimeField(default=datetime.now())
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    amount = models.DecimalField(decimal_places=2, max_digits=5)
    recurring = models.BooleanField(default=False)
    recurrance_type = models.ForeignKey(RecurranceType, null=True, blank=True)

    class Meta:
        abstract = True
        unique_together = ['incurred_date', 'name']

    def __unicode__(self):
        return self.name


class Expense(Entry):
    category = models.ForeignKey(ExpenseCategory)


admin.site.register(Expense)


class Income(Entry):
    category = models.ForeignKey(IncomeCategory)

admin.site.register(Income)



