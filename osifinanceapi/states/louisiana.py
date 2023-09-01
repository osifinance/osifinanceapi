def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
    Income Taxes
    Sources - https://revenue.louisiana.gov/individualincometax
    Summary - Married Filing Jointly or Qualifying Surviving Spouse
              Tax Bracket         Rate
              $0 - $25,000        1.85%
              $25,001 - $100,000   3.50%
              $100,001+            4.25%
              
              Single, Head of Household, Married Filing Seperately
              Tax Bracket         Rate
              $0 - $12,500        1.85%
              $12,501 - $50,000   3.50%
              $50,001+            4.25%

    Deductions
    Sources - https://revenue.louisiana.gov/individualincometax
    Summary - Credit OF $1,000 For each dependent or each taxpayer/spouse age 65+

    Standard Deduction
    Sources - https://www.revenue.louisiana.gov/taxforms/6935(11_02)F.pdf
    Summary - Married Filing Jointly or Qualifying Surviving Spouse - $9,000
              Single, Head of Household, Married Filing Seperately - $4,500
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://revenue.louisiana.gov/individualincometax
    Summary - Net short-term and long-term capital gains are taxed as ordinary income.
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://revenue.louisiana.gov/individualincometax
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