from django.db import models

class Citizenship(models.TextChoices):
    US_CITIZEN = "US Citizen", "US Citizen"
    PERMANENT_RESIDENT_ALIEN = "Permanent Resident Alien", "Permanent Resident Alien"
    NON_PERMANENT_RESIDENT_ALIEN = "Non Permanent Resident Alien", "Non Permanent Resident Alien"

class MaritalStatus(models.TextChoices):
  MARRIED = "Married", "Married"
  SEPARATED = "Separated", "Separated"
  SINGLE = "Single", "Single"
  DIVORCED = "Divorced", "Divorced"

class TypeOfCredit(models.TextChoices):
  INDIVIDUAL = "Individual", "Individual"
  JOINT = "Joint", "Joint"

class Ethnicity(models.TextChoices):
  HISPANIC_LATINO = "Hispanic or Latino", "Hispanic or Latino"
  NOT_HISPANIC_LATINO = "Not Hispanic or Latino", "Not Hispanic or Latino"

class Race(models.TextChoices):
  AMERICAN_INDIAN_ALASKAN_NATIVE = "American Indian or Alaskan Native", "American Indian or Alaskan Native"
  BLACK_AFRICAN_AMERICAN = "Black or African American", "Black or African American"
  ASIAN_INDIAN = "Asian Indian", "Asian Indian"
  CHINESE = "Chinese", "Chinese"
  FILIPINO = "Filipino", "Filipino"
  JAPANESE = "Japanese", "Japanese"
  KOREAN = "Korean", "Korean"
  VIETNAMESE = "Vietnamese", "Vietnamese"
  NATIVE_HAWAIIAN_PACIFIC_ISLANDER = "Native Hawaiian or Other Pacific Islander", "Native Hawaiian or Other Pacific Islander"
  WHITE = "White", "White"

class Gender(models.TextChoices):
  MALE = "Male", "Male"
  FEMALE = "Female", "Female"

class Borrower(models.Model):
  first_name = models.CharField(max_length=60)
  last_name = models.CharField(max_length=60)
  middle_name = models.CharField(max_length=60, null=True, blank=True)
  ssn = models.CharField(max_length=12)
  date_of_birth = models.DateField()
  citizenship = models.CharField(max_length=60, choices=Citizenship.choices)
  type_of_credit = models.CharField(max_length=30, choices=TypeOfCredit.choices)
  marital_status = models.CharField(max_length=30, choices=MaritalStatus.choices)
  email = models.CharField(max_length=100)
  dependents = models.SmallIntegerField(null=True, blank=True)
  dependent_ages = models.CharField(max_length=60, null=True, blank=True)
  ethicity = models.CharField(max_length=60, choices=Ethnicity.choices, null=True)
  race = models.CharField(max_length=60, choices=Race.choices, null=True)
  gender = models.CharField(max_length=30, choices=Gender.choices, null=True)


class PhoneNumber(models.Model):
  PHONE_NUMBER_TYPE = [
    ('Home', 'Home'),
    ('Cell', 'Cell'),
    ('Work', 'Work')
  ]
  borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
  phone_number = models.CharField(max_length=20)
  phone_number_type = models.CharField(max_length=10, choices=PHONE_NUMBER_TYPE)
  phone_number_ext = models.CharField(max_length=10, null=True, blank=True)  

class State(models.TextChoices):
  AL = "AL", "Alabama"
  AZ = "AZ", "Arizona"
  AR = "AR", "Arkansas"
  CA = "CA", "California"
  CO = "CO", "Colorado"
  CT = "CT", "Connecticut"
  DE = "DE", "Delaware"
  FL = "FL", "Florida"
  GA = "GA", "Georgia"
  IL = "IL", "Illinois"
  IN = "IN", "Indiana"
  KS = "KS", "Kansas"
  KY = "KY", "Kentucky"
  LA = "LA", "Louisiana"
  MD = "MD", "Maryland"
  MA = "MA", "Massachusetts"
  MI = "MI", "Michigan"
  MN = "MN", "Minnesota"
  MS = "MS", "Mississippi"
  MO = "MO", "Missouri"
  MT = "MT", "Montana"
  NE = "NE", "Nebraska"
  NV = "NV", "Nevada"
  NH = "NH", "New Hampshire"
  NJ = "NJ", "New Jersey"
  NM = "NM", "New Mexico"
  NY = "NY", "New York"
  NC = "NC", "North Carolina"
  ND = "ND", "North Dakota"
  OK = "OK", "Oklahoma"
  OR = "OR", "Oregon"
  PA = "PA", "Pennsylvania"
  RI = "RI", "Rhode Island"
  SC = "SC", "South Carolina"
  SD = "SD", "South Dakota"
  TN = "TN", "Tennessee"
  TX = "TX", "Texas"
  VT = "VT", "Vermont"
  VA = "VA", "Virginia"
  WA = "WA", "Washington"
  WV = "WV", "West Virginia"
  WI = "WI", "Wisconsin"
  WY = "WY", "Wyoming"

class Address(models.Model):

  class HousingType(models.TextChoices):
    OWN = "Own", "Own"
    RENT = "Rent", "Rent"
    NO_EXPENSE = "No primary housing expense", "No primary housing expense"

  class AddressType(models.TextChoices):
    CURRENT = "Current", "Current"
    FORMER = "Former", "Former"

  class Meta:
    verbose_name = "Address"
    verbose_name_plural = "Addresses"

  borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
  street_address = models.CharField(max_length=150)
  unit = models.CharField(max_length=100, null=True, blank=True)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=2, choices=State.choices)
  zip_code = models.CharField(max_length=20)
  country = models.CharField(max_length=100)
  address_type = models.CharField(max_length=20, choices=AddressType.choices)
  years_at = models.SmallIntegerField()
  months_at = models.SmallIntegerField()
  housing_type = models.CharField(max_length=100, choices=HousingType.choices)
  rent_per_month = models.FloatField(null=True, blank=True)

class Employment(models.Model):
  class EmploymentType(models.TextChoices):
    CURRENT = "Current", "Current"
    PREVIOUS = "Previous", "Previous"
  
  borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
  employer_name = models.CharField(max_length=100)
  street_address = models.CharField(max_length=100)
  unit = models.CharField(max_length=60, null=True, blank=True)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=2, choices=State.choices)
  zip_code = models.CharField(max_length=20)
  country = models.CharField(max_length=100)
  position = models.CharField(max_length=100)
  employer_type = models.CharField(max_length=20, choices=EmploymentType.choices)
  start_date = models.DateField()
  end_date = models.DateField(null=True, blank=True)
  previous_gross_monthly_income = models.FloatField()
  is_owned = models.BooleanField()
  base_pay_per_month = models.FloatField()
  overtime_pay_per_month = models.FloatField(null=True, blank=True)
  bonus_per_month = models.FloatField(null=True, blank=True)
  commission_per_month = models.FloatField(null=True, blank=True)
  military_entitlements_per_month = models.FloatField(null=True, blank=True)
  other_pay_per_month = models.FloatField(null=True, blank=True)

  

class IncomeSourceCategory(models.TextChoices):
    ALIMONY = "Alimony", "Alimony"
    AUTOMOBILE_ALLOWANCE = "Automobile Allowance", "Automobile Allowance"
    BOARDER_INCOME = "Boarder Income", "Boarder Income"
    CAPITAL_GAIN = "Capital Gains", "Capital Gains"
    CHILD_SUPPORT = "Child Support", "Child Support"
    DISABILITY = "Disability", "Disability"
    FOSTER_CARE = "Foster Care", "Foster Care"
    HOUSING = "Housing", "Housing"
    PARSONAGE = "Parsonage", "Parsonage"
    INTEREST_DIVIDENDS = "Interest and Dividends", "Interest and Dividends"
    MORTGAGE_CREDIT_CERTIFICATE = "Mortgage Credit Certificate", "Mortgage Credit Certificate"
    MORTGATE_DIFFERENTIAL = "Mortgage Differential", "Mortgage Differential" 
    PAYMENTS = "Payments", "Payments"
    NOTE_RECEIVABLE = "Notes Receivable", "Notes Receivable"
    PUBLIC_ASSISTANCE = "Public Assistance", "Public Assistance"
    PENSION = "Pension", "Pension"
    IRA = "IRA", "IRA"
    ROYALTY_PAYMENT = "Royalty Payments", "Royalty Payments"
    SEPARATE_MAINTENACE = "Separate Maintenance", "Separate Maintenance"
    SOCIAL_SECURITY = "Social Security", "Social Security"
    TRUST = "Trust", "Trust"
    UNEMPLOYMENT = "Unemployment", "Unemployment"
    VA_COMENSATION = "VA Compensation", "VA Compensation"
    OTHER = "Other", "Other"

class IncomeSource(models.Model):
  borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
  income_source = models.CharField(max_length=100, choices=IncomeSourceCategory.choices)
  monthly_income = models.FloatField()

class AssetAccountType(models.TextChoices):
  CHECKING = "Checking", "Checking"
  SAVINGS = "Savings", "Savings"
  MONEY_MARKET = "Money Market", "Money Market"
  CERTIFICATE_OF_DEPOSIT = "Certificate of Deposit", "Certificate of Deposit"
  MUTUAL_FUND = "Mutual Fund", "Mutual Fund"
  STOCK = "Stocks", "Stocks"
  STOCK_OPTIONS = "Stock Options", "Stock Options"
  BONDS = "Bonds", "Bonds"
  RETIREMENT = "Retirement", "Retirement"
  BRIDGE_LOAN_PROCEEDS = "Bridge Loan Proceeds", "Bridge Loan Proceeds"
  INDIVIDUAL_DEVELOPEMNT_ACCOUNT = "Individual Development Account", "Individual Development Account"
  TRUST_ACCOUNT = "Trust Account", "Trust Account"
  CASH_VALUE_OF_LIEF_INSURANCE = "Cash Value of Life Insurance", "Cash Value of Life Insurance"
  

class Asset(models.Model):
  borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
  account_type = models.CharField(max_length=100, choices=AssetAccountType.choices)
  financial_institution = models.CharField(max_length=100)
  account_number = models.CharField(max_length=100)
  cash_market_value = models.FloatField()

class OtherAccessAccountCreditType(models.TextChoices):
  OTHER_ASSET_PROCEEDS_FROM_REAL_ESTATE = "Proceeds from Real Estate Property to be sold on or before closing" 
  OTHER_ASSET_PROCEEDS_FROM_NON_REAL_ESTATE = "Proceeds from Sale of Non-Real Estate Asset"
  OTHER_ASSET_SECURED_BORROWED_FUNDS = "Secured Borrowed Funds"
  OTHER_ASSET_UNSECURED_BORROWED_FUNDS = "Unsecured Borrowed Funds"
  OTHER_ASSET = "Other"
  CREDIT_EARNEST_MONEY = "Earnest Money", "Earnest Money"
  CREDIT_EMPLOYER_ASSISTANCE = "Employer Assistance", "Employer Assistance"
  CREDIT_LOT_EQUITY = "Lot Equity", "Lot Equity"
  CREDIT_RELOCATION_FUNDS = "Relocation Funds", "Relocation Funds"
  CREDIT_RENT_CREDIT = "Rent Credit", "Rent Credit"
  CREDIT_SWEAT_QUITY = "Sweat Equity", "Sweat Equity"
  CREDIT_TRADE_EQUITY = "Trade Equity", "Trade Equity "
  
class OtherAssetsCreditsAccount(models.Model):
  borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
  asset_credit_type = models.CharField(max_length=100, choices=OtherAccessAccountCreditType.choices)
  cash_market_value = models.FloatField()

class LiabilityAccounType(models.TextChoices):
  REVOLVING = "Revolving", "Revolving"
  INSTALLMENT = "Installment", "Installment"
  OPEN_30_DAY = "Open 30-Day", "Open 30-Day"
  LEASE = "Lease", "Lease"
  OTHER = "Other", "Other"

class Liability(models.Model):
  class Meta:
    verbose_name = "Liability"
    verbose_name_plural = "Liabilities"

  borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
  account_type = models.CharField(max_length=100, choices=LiabilityAccounType.choices)
  company_name = models.CharField(max_length=100)
  account_number = models.CharField(max_length=100)
  unpaid_balance = models.FloatField()
  paid_off_before_or_at_closing = models.BooleanField()
  monthly_payment = models.FloatField()

class OtherLiabilityExpenseType(models.TextChoices):
  ALIMONY = "Alimony", "Alimony"
  CHILD_SUPPORT = "Child Support", "Child Support"
  SEPARATE_MAINTENANCE = "Separate Maintenance", "Separate Maintenance" 
  JOB_RELATED_EXPENSES = "Job Related Expenses", "Job Related Expenses"
  OTHER = "Other", "Other"

class OtherLiabilityExpense(models.Model):
  class Meta:
    verbose_name = "Other Liability Expense"
    verbose_name_plural = "Other Liability Expenses"

  borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
  liability_expense_type = models.CharField(max_length=100, choices=OtherLiabilityExpenseType)
  monthly_paymnet = models.FloatField()

class RealEstateProperty(models.Model):
  class Meta:
    verbose_name = "RealEstateProperty"
    verbose_name_plural = "Real Estate Properties"

  class Status(models.TextChoices):
    SOLD = "Sold", "Sold"
    PENDING_SALE = "Pending Sale", "Pending Sale"
    RETAINED = "Retained", "Retained"

  class IntendedOccupancy(models.TextChoices):
    INVESTMENT = "Investment", "Investment"
    PRIMARY_RESIDENCE = "Primary Residence", "Primary Residence"
    SECOND_HOME = "Second Home", "Second Home"
    OTHER = "Other", "Other"

  borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
  street_address = models.CharField(max_length=150)
  unit = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=2, choices=State.choices)
  zip_code = models.CharField(max_length=20)
  country = models.CharField(max_length=100)
  property_value = models.FloatField()
  monthly_insurance_tax_association_due = models.FloatField()
  monthly_rental_income = models.FloatField()
  net_monthly_rental_income = models.FloatField()

class RealEstateProperyMortgageLoan(models.Model):
  class MortageType(models.TextChoices):
    FHA = "FHA", "FHA"
    CONVENTIONAL = "Conventional", "Conventional"
    USDA_RD = "USDA-RD","USDA-RD"
    OTHER = "Other", "Other"

  borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
  real_estate_property = models.ForeignKey(RealEstateProperty, on_delete=models.CASCADE)
  creditor_name = models.CharField(max_length=100)
  account_number = models.CharField(max_length=100)
  monthly_mortgage_payment = models.FloatField()
  unpaid_balance = models.FloatField()
  paid_off_before_or_at_closing = models.BooleanField()
  mortgage_loan_type = models.CharField(max_length=30, choices=MortageType.choices)
  credit_limit = models.FloatField()

class LoanPropertyInfo(models.Model):
  class Meta:
    verbose_name = "Loan Property Information"

  class LoanPurpose(models.TextChoices):
    PURCHASE = "Purchase", "Purchase"
    REFINANCE = "Refinance", "Refinance"
    OTHER = "Other", "Other"

  class Occupancy(models.TextChoices):
    PRIMARY_RESIDENCE = "Primary Residence", "Primary Residence"
    SECOND_HOME = "Second Home", "Second Home"
    INVESTMENT_PROPERTY = "Investment Property", "Investment Property"
    FHA_SECONDARY_HOME = "FHA Secondary Home", "FHA Secondary Home"

  borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
  loan_amount = models.FloatField()
  loan_purpose = models.CharField(max_length= 30, choices=LoanPurpose.choices)
  other_purpose = models.CharField(max_length=100)
  property_address = models.CharField(max_length=150)
  property_unit = models.CharField(max_length=100)
  property_city = models.CharField(max_length=100)
  property_state = models.CharField(max_length=2, choices=State.choices)
  property_zip_code = models.CharField(max_length=20)
  property_country = models.CharField(max_length=100)
  property_number_of_units = models.IntegerField()
  property_value = models.FloatField()
  occupancy = models.CharField(max_length=100, choices=Occupancy.choices)
  is_mixed_use_of_property = models.BooleanField()
  is_manufactured_home = models.BooleanField()
  expected_rental_income = models.FloatField()

class GiftGrant(models.Model):
  class AssetType(models.TextChoices):
    CASH_GIFT = "Cash Gift", "Cash Gift"
    GIFT_OF_EQUITY = "Gift of Equity", "Gift of Equity"
    GRANT = "Grant", "Grant"

  class SourceList(models.TextChoices):
    COMMUNITY_NONPROFIT = "Community Nonprofit", "Community Nonprofit"
    EMPLOYER = "Employer", "Employer"
    FEDERAL_AGENCY = "Federal Agency", "Federal Agency"
    LOCAL_AGENCY = "Local Agency", "Local Agency"
    RELATIVE = "Relative", "Relative"
    RELIGIOUS_NONPROFIT = "Religious Nonprofit", "Religious Nonprofit"
    STATE_AGENCY = "State Agency", "State Agency"
    UNMARRIED_PARTNER = "Unmarried Partner", "Unmarried Partner"
    LENDER = "Lender", "Lender"
    OTHER = "Other", "Other"

  # borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
  loan_property_info = models.ForeignKey(LoanPropertyInfo, on_delete=models.CASCADE)
  asset_type = models.CharField(max_length=100, choices=AssetType.choices)
  deposited = models.BooleanField()
  not_deposited = models.BooleanField()
  source = models.CharField(max_length=100, choices=SourceList.choices)
  cash_market_value = models.FloatField()

class Declaration(models.Model):
  borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
  occupy_as_primary_residence = models.BooleanField()
  has_relationship_with_seller = models.BooleanField()
  is_borrowing_from_other_party = models.BooleanField()
  is_applying_for_another_mortgage = models.BooleanField()
  is_applying_for_new_credit = models.BooleanField()
  is_subject_to_a_lien = models.BooleanField()
  is_cosigner_or_guarantor_on_undisclosed_debt = models.BooleanField()
  is_any_other_judgements = models.BooleanField()
  has_law_suit_with_potential_liability = models.BooleanField()
  has_conveyed_title_in_lieu_of_forclosure_last_7_years = models.BooleanField()
  has_declared_bankrupcy_with_past_7_years = models.BooleanField()
