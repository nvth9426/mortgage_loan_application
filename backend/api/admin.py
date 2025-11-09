from django.contrib import admin
from .models import *


class AddressInline(admin.TabularInline):
  model = Address
  extra = 2
  # list_display = ('street_address', 'unit', 'city', 'state', 'zip_code', 'address_type', 'housing_type')

class PhoneNumberInline(admin.TabularInline):
  model = PhoneNumber
  # extra = 1
  # list_display = ('phone_number', 'phone_number_ext', 'phone_number_type')

class EmploymentInline(admin.TabularInline):
  model = Employment
  extra = 2

class IncomeSourceInlline(admin.TabularInline):
  model = IncomeSource

class AssetInline(admin.TabularInline):
  model = Asset

class OtherAssetsCreditsAccountInline(admin.TabularInline):
  model = OtherAssetsCreditsAccount

class LiabilityInline(admin.TabularInline):
  model = Liability

class OtherLiabilityExpensesInline(admin.TabularInline):
  model = OtherLiabilityExpenses

class BorrowerAdmin(admin.ModelAdmin):
  inlines = [AddressInline,
             PhoneNumberInline,
             EmploymentInline,
             IncomeSourceInlline,
             AssetInline,
             OtherAssetsCreditsAccountInline,
             LiabilityInline,
             OtherLiabilityExpensesInline]
  
  list_display = ('first_name', 'last_name')  

admin.site.register(Borrower, BorrowerAdmin)

