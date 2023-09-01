def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income ='''
    Income Taxes (2023)
    Sources- https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2022-760-instructions.pdf (P. 35)
    Summary - If your AGI is:
              Over      But not over       Tax is:
              $0        $3,00              2% of AGI
              $3,000    $5,000             $60 plus 3% of the amount over $3,000
              $5,000    $17,000            $120 plus 5% of the amount over $17,000
              $17,000                      $720 plus 5.75% of the amount over $17,000

    
    Standard Deduction
    Sources- https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2022-760-instructions.pdf (P.1)
    Summary - $16,000 for married filers filing jointly, $8,000 otherwise

    Dependent Deduction
    Sources - https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2022-760-instructions.pdf (P.10)
    Summary - $930 per dependent

    Age 65 or Older Deduction
    Sources - https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2022-760-instructions.pdf (P.10)
    Summary - $800 per spouse age 65 or older

    Reciprocal Agreements
    Sources - https://www.tax.virginia.gov/reciprocity
    Summary - District of Columbia, Kentucky, Maryland, Pennsylvania, and West Virginia
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2022-760-instructions.pdf
    Summary - Net short-term and long-term capital gains are taxed as ordinary income.
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2022-760-instructions.pdf
    Summary - No local jurisdictions impose additional income taxes
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
