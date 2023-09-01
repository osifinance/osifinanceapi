def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
    Income Taxes
    Sources - https://dor.georgia.gov/tax-tables-georgia-tax-rate-schedule
    Summary - Single
              If Georgia Taxable Income Is
              Over        But not over    Amount of Tax Is
              $0          $750            1% of taxable income
              $750        $2,250          $8.00 Plus 2% of the amount over $750
              $2,250      $3,750          $38.00 Plus 3% of the amount over $2,250
              $3,750      $5,250          $83.00 Plus 4% of the amount over $3,750
              $5,250      $7,000          $143.00 Plus 5% of the amount over $5,250
              $7,000                      $230.00 Plus 5.75% of the amount over $7,000
          
              Married Filing Joint or Head of Household
              If Georgia Taxable Income Is
              Over        But not over    Amount of Tax Is
              $0          $1,000          1% of taxable income
              $1,000      $3,000          $10.00 Plus 2% of the amount over $1,000
              $3,000      $5,000          $50.00 Plus 3% of the amount over $3,000
              $5,000      $7,000          $110.00 Plus 4% of the amount over $5,000
              $7,000      $10,000         $190.00 Plus 5% of the amount over $7,000
              $10,000                     $340.00 Plus 5.75% of the amount over $10,000
          
              Married Filing Separate
              If Georgia Taxable Income Is
              Over        But not over    Amount of Tax Is
              $0          $500            1% of taxable income
              $500        $1,500          $5.00 Plus 2% of the amount over $500
              $1,500      $2,500          $25.00 Plus 3% of the amount over $1,500
              $2,500      $3,500          $55.00 Plus 4% of the amount over $2,500
              $3,500      $5,000          $95.00 Plus 5% of the amount over $3,500
              $5,000                      $170.00 Plus 5.75% of the amount over $5,000

    Standard Deduction
    Sources - https://apps.dor.ga.gov/FillableForms/PDFViewer/Index?form=2022GA500 (Lines 6c., 14a.)
    Summary - Married Filing Jointly: $7,400
              Single or Head of Household: $2,700
              Married Filing Separately: $3,700

    Dependent Deduction
    Sources - https://apps.dor.ga.gov/FillableForms/PDFViewer/Index?form=2022GA500 (Lines 7a., 14b.)
    Summary - $3,000 for each dependent 

    Age 65+ Deduction
    Sources - Sources - https://apps.dor.ga.gov/FillableForms/PDFViewer/Index?form=2022GA500 (Line 11 b.)
    Summary - $1,300 per person 
'''
doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://dor.georgia.gov/years-individual-income-tax-forms
    Summary - Short-term capital gains are taxed as ordinary income.
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://dor.georgia.gov/years-individual-income-tax-forms
    Summary - No jurisdictions impose additional income taxes
    '''

@add_doc(doc_income+doc_capital_gains+doc_local)
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