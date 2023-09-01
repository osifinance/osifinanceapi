def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
    Income Taxes
    Sources - https://www.tax.nd.gov/forms
              https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2022-iit/2022-individual-income-tax-booklet.pdf
    Summary - Single
              If North Dakota Taxable Income Is:
              Over        But Not Over    Your Tax Is: 
              $0          $41,775         1.10% of North Dakota Taxable Income   
              $41,775     $101,050        $459.53 + 2.04% of amount over $41,775
              $101,050    $210,825        $1,668.74 + 2.27% of amount over $101,050
              $210,825    $458,350        $4,160.63 + 2.64% of amount over $210,825
              $458,350                    $10,695.29 + 2.90% of amount over $458,350

              Married Filing Joint and Qualifying Surviving Spouse
              If North Dakota Taxable Income Is:
              Over        But Not Over     Your Tax Is:
              $0          $69,700          1.10% of North Dakota Taxable Income
              $69,700     $168,450         $766.70 + 2.04% of amount over $69,700
              $168,450    $256,650         $2,781.20 + 2.27% of amount over $168,450
              $256,650    $458,350         $4,783.34 + 2.64% of amount over $256,650
              $458,350                     $10,108.22 + 2.90% of amount over $458,350
              
              Married Filing Separately
              If North Dakota Taxable Income Is:
              Over        But Not Over     Your Tax Is:
              $0          $34,850          1.10% of North Dakota Taxable Income
              $34,850     $84,225          $766.70 + 2.04% of amount over $34,850
              $84,225     $128,325         $2,781.20 + 2.27% of amount over $84,225
              $128,325    $229,175         $4,783.34 + 2.64% of amount over $128,325
              $229,175                     $5,054.11 + 2.90% of amount over $229,175

    Standard Deduction
    Sources - https://www.tax.nd.gov/sites/www/files/documents/forms/2022-individual-income-tax-booklet.pdf (P. 12)
    Summary - Same as federal

    Credits
    Sources - https://www.tax.nd.gov/tax-exemptions-credits/income-tax-exemptions-credits

    Reciprocal Agreements
    Sources - https://www.tax.nd.gov/sites/www/files/documents/forms/business/ndwrfillable.pdf
    Summary - Minnesota and Montana
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://www.tax.nd.gov/news/tax-legislative-changes/significant-changes-law/individual-income-tax-history
    Summary - 40% of the long-term gains are deducted from adjusted gross income (AGI)
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://www.tax.nd.gov/forms
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
