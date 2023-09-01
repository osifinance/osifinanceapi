def add_doc(value):
    import os
    def _doc(func):
        func.__doc__ = os.path.basename(__file__).title() + value
        return func
    return _doc

doc_income = '''
    Income Taxes
    Sources - https://www.ksrevenue.gov/taxrates.html
    Summary - Tax year 2018 and all tax years thereafter
              Tax Rates, Resident, married, joint
                  taxable income not over $30,000: 3.1 % (K.S.A. 79-32,110)
                  taxable income over $30,000 but not over $60,000: $930 plus 5.25 % of excess over $30,000 (K.S.A. 79-32,110)
                  taxable income over $60,000: $2,505 plus 5.7 % of excess over $60,000 (K.S.A. 79-32,110)
              Tax Rates, Resident, others
                  taxable income not over $15,000: 3.1 % (79-32,110)
                  taxable income over $15,000 but not over $30,000: $465 plus 5.25 % of excess over $15,000 (K.S.A. 79-32,110)
                  taxable income over $30,000: $1252.50 plus 5.7 % of excess over $30,000 (K.S.A. 79-32,110)

    Standard Deduction
    Sources - https://www.ksrevenue.gov/incomebook22.html#0 (Line 4)
    Summary - Single: $3,500
              Married Filing Jointly: $8,000
              Married Filing Separately: $4,000
              Head of Household: $6,000

    Age 65+ Deduction
    Sources - https://www.ksrevenue.gov/incomebook22.html#0 (Line 4)
    Summary - $850 if single or head of household
              $700 per spouse if married filing jointly or separately
    Exemptions
    Sources - https://www.ksrevenue.gov/incomebook22.html#0 (Line 5)
    Summary - $2,250 per indvidual/spouse or dependent
    '''

doc_capital_gains = '''
    Capital Gains Taxes
    Sources - https://www.ksrevenue.gov/incomebook22.html
    Summary - Net short-term and long-term capital gains are taxed as ordinary income.
    '''

doc_local = '''
    Local Income Taxes
    Sources - https://www.ksrevenue.gov/incomebook22.html
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