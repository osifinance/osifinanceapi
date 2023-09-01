def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
    Income Taxes
    Sources - https://tax.vermont.gov/sites/tax/files/documents/GB-1210-2023.pdf (Only Single and Married Filing Jointly?)
              https://tax.vermont.gov/sites/tax/files/documents/Income%20Booklet-2022.pdf (P. 45) For Comparison
    Summary -  Married Filing Jointly
              If Wages are:
              over         but not over   Tax is:
              $0           $10,538        $0
              $10,538      $86,388        3.35% of amount over $10,538
              $86,388      $193,938       $2,540.98 + 6.60% of amount over $86,388
              $193,938     $289,988       $9,639.28 + 7.60% of amount over $193,938
              $289,988                    $16,939.08 + 8.75% of amount over 289,988
          
              Other Filers
              If Wages are:
              over         but not over   Tax is:
              $0           $3,500         $0
              $3,500       $48,900        3.35% of amount over $3,500
              $48,900      $113,550       $1,520.90 + 6.60% of amount over $48,900
              $113,550     $233,050       $5,787.80 + 7.60% of amount over $113,550
              $233,050                    $14,869.80 + 8.75% of amount over #233,050

    Special Clause
    Sources - https://tax.vermont.gov/sites/tax/files/documents/Income%20Booklet-2022.pdf (P. 45) For Comparison (P. 11, Line 8)
    Summary - If AGI is more than $150,000, the filer must pay a minimum of 3%

    Deductions and Exemptions
    Sources - https://tax.vermont.gov/sites/tax/files/documents/Income%20Booklet-2022.pdf (P. 10)
    Summary - Standard Deduction
              Single or Married Filing Separately: $6,800
              Married Filing Jointly $13,050
              Head of Household: $9,800
          
              $4,500 per individual/spouse, dependent
              $1,050 per individual/spouse over 65

    Credits
    Sources - https://tax.vermont.gov/individuals/personal-income-tax/tax-credits
    Summary - Dependent based:
                  "72% of the federal Child and Dependent Care Tax Credit"
                  "Fully refundable"
              EIC based:
                  "38% of the federal Earned Income Tax Credit"
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://tax.vermont.gov/individuals/personal-income-tax/taxable-income
    Summary - 40% of long capital gains of assets held for more than 3 years up to $350,000 in deductions
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://tax.vermont.gov/individuals/personal-income-tax/local-option-tax
    Summary - No local jurisdictions impose additional income taxes
    '''

@add_doc(doc_income+doc_capital_gains)
def total(filing_status="single", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0, filers_over_65=0):
    return 1

@add_doc(doc_income)
def income(filing_status="single", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0, filers_over_65=0):
    return 2
    
@add_doc(doc_capital_gains)
def capital_gains(filing_status="single", capital_gains_short=0, capital_gains_long=0, credits_state=0, state_agi=0, income=0, dependents=0, filers_over_65=0):
    return 3

@add_doc(doc_local)
def local():
    return 4
