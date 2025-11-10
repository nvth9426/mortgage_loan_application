from django.contrib import admin
from .models import *

class AddressInline(admin.TabularInline):
  model = Address
  extra = 1
  # list_display = ('street_address', 'unit', 'city', 'state', 'zip_code', 'address_type', 'housing_type')

class PhoneNumberInline(admin.TabularInline):
  model = PhoneNumber
  extra = 1

class EmploymentInline(admin.TabularInline):
  model = Employment
  extra = 1

class IncomeSourceInlline(admin.TabularInline):
  model = IncomeSource
  extra = 1

class AssetInline(admin.TabularInline):
  model = Asset
  extra = 1

class OtherAssetsCreditsAccountInline(admin.TabularInline):
  model = OtherAssetsCreditsAccount
  extra = 1

class LiabilityInline(admin.TabularInline):
  model = Liability
  extra = 1

class OtherLiabilityExpensesInline(admin.TabularInline):
  model = OtherLiabilityExpense
  extra = 1

class RealEstatePropertyInline(admin.TabularInline):
  model = RealEstateProperty
  extra = 1

class RealEstateProperyMortgageLoanInline(admin.TabularInline):
  model = RealEstateProperyMortgageLoan
  extra = 1

class LoanPropertyInfoStackedInLine(admin.StackedInline):
  model = LoanPropertyInfo
  max_num = 1
  extra = 1

class GiftGrantInline(admin.TabularInline):
  model = GiftGrant

class DeclarationStackedInline(admin.TabularInline):
  max_num = 1
  extra = 1
  model = Declaration

class BorrowerAdmin(admin.ModelAdmin):
  inlines = [AddressInline,
             PhoneNumberInline,
             EmploymentInline,
             IncomeSourceInlline,
             AssetInline,
             OtherAssetsCreditsAccountInline,
             LiabilityInline,
             OtherLiabilityExpensesInline,
             RealEstatePropertyInline,
             RealEstateProperyMortgageLoanInline,
             LoanPropertyInfoStackedInLine,
            #  GiftGrantInline,
             DeclarationStackedInline]
  
  list_display = ('first_name', 'last_name', 'get_phone_number')  

  @admin.display(description='Phone Number')
  def get_phone_number(self, obj):  
    return f"{obj.phonenumber_set.filter(phone_number_type='Home').first().phone_number}"

admin.site.register(Borrower, BorrowerAdmin)
admin.site.register(GiftGrant)
